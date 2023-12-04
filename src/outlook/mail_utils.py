from .create_accounts_utils import getaccpetbtn, getaccpetbtnselector, keep_clicking_till_page_not_change, keep_getting_element
from botasaurus import *

def get_profile(data):
    return data['username']


def get_proxy(data):
    return data['proxy']


def get_visited_emails(driver):
    return driver.execute_script("return window.emails")


def login_outlook(driver:AntiDetectDriver, password):
    getaccpetbtn(driver)
    driver.type('[type="password"]', password )
    keep_clicking_till_page_not_change(driver, getaccpetbtnselector())

def wait_till_load(driver):
    keep_getting_element(driver, "#MailList")


def run_till_get_emails(driver):
    while type (get_visited_emails(driver)) is not list:
        driver.execute_file('spy-email.js')


def load_outlook(driver:AntiDetectDriver, username, spy_emails):
    driver.get("https://outlook.live.com/mail/0/")

    if spy_emails: 
        run_till_get_emails(driver)

    btn = None
    while btn is None:
        btn = driver.get_element_or_none_by_selector("#MailList", 0.4)
        if spy_emails: 
            run_till_get_emails(driver)

        if driver.is_in_page("login.live.com/login.srf"):
            account = bt.Profile.get_profile(username)  
            login_outlook(driver, account['password'])
            print("logged in")
            return load_outlook(driver, account, spy_emails)

def open_junk_mail(driver:AntiDetectDriver, username, spy_emails):
    # driver.get_by_current_page_referrer("https://outlook.live.com/mail/0/junkemail")
    
    keep_clicking_till_page_not_change(driver, '[data-icon-name="FolderProhibitedRegular"]')

    # document.querySelector().click()

    # if spy_emails: 
    #     run_till_get_emails(driver)

    # btn = None
    # while btn is None:
    #     btn = driver.get_element_or_none_by_selector("#MailList", 0.4)
    #     if spy_emails: 
    #         run_till_get_emails(driver)

    #     if driver.is_in_page("login.live.com/login.srf"):
    #         account = bt.Profile.get_profile(username)  
    #         login_outlook(driver, account['password'])
    #         print("logged in")
    #         return load_outlook(driver, account)



# def open_junk_mail(driver:AntiDetectDriver, username, spy_emails):
#     driver.execute_script(f"""
#                 document.body.innerHTML = "<div/>"
#                 window.location.href = "https://outlook.live.com/mail/0/junkemail";
#             """)

#     if spy_emails: 
#         run_till_get_emails(driver)

#     btn = None
#     while btn is None:
#         btn = driver.get_element_or_none_by_selector("#MailList", 0.4)
#         if spy_emails: 
#             run_till_get_emails(driver)

#         if driver.is_in_page("login.live.com/login.srf"):
#             account = bt.Profile.get_profile(username)  
#             login_outlook(driver, account['password'])
#             print("logged in")
#             return load_outlook(driver, account)
