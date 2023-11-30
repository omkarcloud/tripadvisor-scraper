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

    btn = driver.get_element_or_none_by_selector("#MailList", bt.Wait.SHORT  * 2)

    if spy_emails: 
        run_till_get_emails(driver)
    if btn is None:
        account =bt.Profile.get_item(username)  
        if driver.is_in_page("login.live.com/login.srf"):
            login_outlook(driver, account['password'])
            print("logged in")
            return load_outlook(driver, account)
        else:
            wait_till_load(driver)
