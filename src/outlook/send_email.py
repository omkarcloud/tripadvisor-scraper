from .browser_attributes import browser_attributes
import time
from botasaurus import *
from .mail_utils import * 
from bs4 import BeautifulSoup
from botasaurus.decorator_helpers import retry_on_stale_element

def is_html(html):
    return bool(BeautifulSoup(html, "html.parser").find())

@retry_on_stale_element
def send_email(driver:AntiDetectDriver, to, subject, body):
    
    el = driver.get_element_or_none_by_selector('[role="main"] [role="textbox"]')
    if el is None:
        driver.click('[data-icon-name="MailRegular"]')

    # Step 2: Clear and type "t" in the first element of [role="main"] [role="textbox"]
    first_textbox = driver.get_elements_or_none_by_selector('[role="main"] [role="textbox"]')[0]
    first_textbox.clear()
    first_textbox.send_keys(to)

    if subject:
        # Step 4: Clear and type "t" in [role="main"] [type="text"]
        text_input = driver.get_element_or_none_by_selector( '[role="main"] [type="text"]')
        
        
        text_input.clear()
        text_input.send_keys(subject)

    # Step 3: Clear and type "t" in the last element of [role="main"] [role="textbox"]
    last_textbox = driver.get_elements_or_none_by_selector( '[role="main"] [role="textbox"]')[-1]
    
    if is_html(body):
        driver.execute_script("arguments[0].innerHTML = arguments[1];", last_textbox, body)
    else:
        last_textbox.clear()
        last_textbox.send_keys(body)

    # Step 5: Click data-icon-name="send"
    driver.click('[data-icon-name="send"], [role="main"] .ms-Button--primary')

    # Step 6: If .ms-Modal-scrollableContent is present, click the primary button
    
    modal_content = driver.get_element_or_none_by_selector('.ms-Modal-scrollableContent', 2)

    while modal_content: # There can be many modals (like forgot subject, forgot attachment), so we need to loop through them
        driver.click(".ms-Modal-scrollableContent .ms-Button--primary")
        time.sleep(2)
        modal_content = driver.get_element_or_none_by_selector('.ms-Modal-scrollableContent', 2)

@browser(
        **browser_attributes,
        output=None
        )
def send_emails(driver:AntiDetectDriver, data):
    # print(driver.about.profile)
    emails = data['emails']
    get_random_delay = data['get_random_delay']
    
    username = data['username']
    load_outlook(driver, username, spy_emails=False)

    for index, email in enumerate(emails):
        send_email(driver, email['to'], email.get('subject', None), email['body'])
        
        # Check if the current email is not the last one in the list
        if index < len(emails) - 1:
            driver.sleep(get_random_delay())
        else:
            pass
            # The last email has been sent, wait just a little more.
            # time.sleep(3)