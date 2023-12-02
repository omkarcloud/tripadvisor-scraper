from botasaurus import *

from .browser_attributes import browser_attributes
from .mail_utils import load_outlook

att = {**browser_attributes }
att["headless"]=False
att["output"]=None

@browser(**att)
def check(driver:AntiDetectDriver, data):
    username = data['username']
    load_outlook(driver, username, spy_emails=False)
    
    print(f"Please manually check the emails for the account '{username}'.")
    driver.prompt("Press Enter once you have checked the emails.")

