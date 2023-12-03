import json
import traceback

from capsolver import UnknownError
from botasaurus.ip_utils import find_ip_details
import time
from botasaurus import *
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
from botasaurus.drivers import AntiDetectFirefoxDriverSeleniumWire, AntiDetectFirefoxDriver
from src.outlook.solve_captcha import solve_captcha
from urllib.parse import urlparse, urlunparse
import sys

def remove_query_params(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Reconstruct the URL without query parameters
    clean_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))

    return clean_url

def keep_getting_element(driver:AntiDetectDriver, selector):
        btn = driver.get_element_or_none_by_selector(selector, bt.Wait.SHORT )
    
        while btn is None:
            btn = driver.get_element_or_none_by_selector(selector, bt.Wait.SHORT )
            # print('regetting element: ', selector, )
        return btn


def wait_till_in_page(driver:AntiDetectDriver, page):
    while not ( page in remove_query_params(driver.current_url)):
        time.sleep(0.5)



def wait_till_signup_page(driver):
    return wait_till_in_page(driver, 'signup.live.com')



def wait_till_accounts_page(driver):
    wait_till_in_page(driver, 'account.microsoft.com')

    keep_getting_element(driver, '[data-bi-id="sh-sharedshell-profile"]')



def keep_clicking_till_page_not_change(driver:AntiDetectDriver, selector, to = None):
        btn = driver.get_element_or_none_by_selector(selector, bt.Wait.LONG )
    
        while btn is None:
            btn = driver.get_element_or_none_by_selector(selector, bt.Wait.LONG )

        currenturl = driver.current_url

        changed = False
        while not changed:
            btn = driver.get_element_or_none_by_selector(selector, bt.Wait.LONG )
            if btn:
                driver.js_click(btn)
                time.sleep(2)
            if currenturl != driver.current_url:
                if to:
                    if to in driver.current_url:
                        changed = True
                else:
                    changed = True
            time.sleep(0.1)



def lisa_move(driver, element):
                return


def lisa_click(driver, element):
                element.click()


def lisa_type(driver:AntiDetectDriver, el, text):
            el.send_keys(text)


def press_next_btn(driver):
                element = driver.get_element_by_id('iSignupAction', bt.Wait.LONG)
                lisa_click(driver, element)


def type_email(driver, email):
            # Fill in the email and check if it's already taken
            emailInput = driver.get_element_by_id('MemberName', bt.Wait.LONG * 3)
            
            if emailInput is None:
                emailInput = driver.get_element_by_id('MemberName', bt.Wait.LONG)
            lisa_type(driver,emailInput, email)
            
            


def has_username_error(driver):
    return driver.get_element_by_id('MemberNameError', bt.Wait.SHORT) is not None
        
def type_password(driver, password):

            passwordinput = driver.get_element_by_id('PasswordInput', bt.Wait.SHORT )
            if passwordinput is None:
                   if has_username_error(driver):
                          raise Exception('Username is already taken. Retrying with new Account.')
                   
                   passwordinput = driver.get_element_by_id('PasswordInput', bt.Wait.LONG * 3)
            
            lisa_type(driver,passwordinput, password)

def verify_username_is_unique(driver):
        pass



def type_first_name(driver, first_name):
            first = driver.get_element_by_id('FirstName', bt.Wait.LONG)
            lisa_type(driver,first, first_name)


def type_last_name(driver, last_name):
            last = driver.get_element_by_id('LastName', bt.Wait.LONG)
            lisa_type(driver,last, last_name)



def type_birth_month(driver, dob_month):
            birthMonth = driver.get_element_by_id('BirthMonth', bt.Wait.LONG)
            lisa_move(driver, birthMonth)

            objectMonth = Select(birthMonth)
            objectMonth.select_by_value(str(dob_month))

def type_birth_year(driver,dob_year):
            birthYear = driver.get_element_by_id('BirthYear', bt.Wait.LONG)
            lisa_type(driver,birthYear, str(dob_year))

def enter_birth_day(driver, dob_day):
            birthDay = driver.get_element_by_id('BirthDay', bt.Wait.LONG)
            lisa_move(driver, birthDay)

            objectDay = Select(birthDay)
            objectDay.select_by_value(str(dob_day))

def accept_notice(driver):
        keep_clicking_till_page_not_change(driver, '[id="id__0"]')
    
def getaccpetbtnselector():
    accpetid = '.inline-block.button-item.ext-button-item .primary, #acceptButton'
    return accpetid

        

def getaccpetbtn(driver:AntiDetectDriver):
    accpetid = getaccpetbtnselector()
    return driver.get_element_or_none_by_selector(accpetid, bt.Wait.LONG)

                
def stay_signed_in(driver:AntiDetectDriver):
        accpetid = getaccpetbtnselector()
        keep_getting_element(driver, accpetid)
    
        dontshowbtn = keep_getting_element(driver, '[name="DontShowAgain"]')
        dontshowbtn.click()
        
        keep_clicking_till_page_not_change(driver, accpetid)

        


def isinnoticepage(driver:AntiDetectDriver):

      notice_page = 'privacynotice.account.microsoft.com/notice'
      return driver.is_in_page(notice_page)



def isinnoticepagewait(driver:AntiDetectDriver):
      notice_page = 'privacynotice.account.microsoft.com/notice'
      return driver.is_in_page(notice_page, bt.Wait.LONG)

def give_consent(driver:AntiDetectDriver):

    while driver.is_in_page('signup.live.com'):
        time.sleep(0.1)

    
    
    will_be_redirected_to_login_page = False

    if isinnoticepagewait(driver):
        will_be_redirected_to_login_page = "login.live.com" in driver.current_url # https://privacynotice.account.microsoft.com/notice?ru=https://login.live.com/login.srf%3fid%3d292666%26opid%3d7636FF0C85603292%26opidt%3d1700994730#/
        accept_notice(driver)

    if will_be_redirected_to_login_page:
        stay_signed_in(driver)
    
    wait_till_accounts_page(driver)
        
def create_firefox(data):
            
            
            try:
                service = Service(executable_path=GeckoDriverManager().install())

                proxy = data.get('proxy') 
                if proxy:
                    selwireOptions = {'proxy': {'http': proxy, 'https': proxy}}
                    driver = AntiDetectFirefoxDriverSeleniumWire(
                                                service=service,
                                                seleniumwire_options=selwireOptions, 
                                            )
                
                

                else:
                    driver = AntiDetectFirefoxDriver(
                                                service=service,
                                            )
                driver.maximize_window()
                return driver
            except ValueError as e:
                if "You have to add GH_TOKEN".lower() in str(e).lower():
                    print(e)
                    print('Visit ')
                    sys.exit(1)
                    # return create_firefox(data)

                else:
                    traceback.print_exc()
                    print('Failed to open Firefox. Retrying...')
                    time.sleep(1)
                    return create_firefox(data)
            except:
                traceback.print_exc()
                print('Failed to open Firefox. Retrying...')
                time.sleep(1)
                return create_firefox(data)
            


def submittoken(driver, token):
    return driver.execute_script('parent.postMessage(JSON.stringify({eventId:"challenge-complete",payload:{sessionToken:"' + token + '"}}),"*")')

def waittillnextbtnloded(driver):
    sl = "button[data-theme='home.verifyButton']"
    el = driver.get_element_or_none_by_selector(sl, bt.Wait.LONG)
    while el is None:
        el = driver.get_element_or_none_by_selector(sl, bt.Wait.LONG)
    return el


def printblob(driver):
    print(driver.execute_file("get_blob.js"))



def getblob(driver):
    blob = driver.execute_file("get_blob.js")
    while type(blob) is not str:
        blob = driver.execute_file("get_blob.js")
        time.sleep(1)
    return blob

def getua(driver):
    return driver.execute_script("return navigator.userAgent;")
       

def makeblob( blob):
        data = {"blob":blob} 
        return json.dumps(data)       


def getiframeelement(driver):
    return driver.get_element_or_none_by_selector('iframe#enforcementFrame', bt.Wait.SHORT)

def getphoneverificationelement(driver:AntiDetectDriver):
    return driver.get_element_or_none_by_selector('.text-title.forSmsHip', None)   

def getphoneverificationelementwithwait(driver):
    return driver.get_element_or_none_by_selector('.text-title.forSmsHip', bt.Wait.SHORT)   


def get_captcha_id(driver:AntiDetectDriver):
      id = driver.get_element_or_none_by_selector('iframe[data-e2e="enforcement-frame"]', None)
      if id:
            id = id.get_attribute('src')
      
      return id

def solvecaptcha_with_captcha_solver(driver:AntiDetectDriver, proxy = None, captcha=None, capsolver_apikey=None):

    blob = makeblob(getblob(driver))
    
    #bt.prompt("Press Enter When Next Button is Visible")
    
    # first check if token submit works
    # then next check
    # can be simple get source of frame till we can find the home.verifyButton string

    # todo: next btn wait, for now just see console

    iframe = getiframeelement(driver)  
    iframe.is_displayed()
    driver.switch_to.frame(iframe)

    
    try:
        token = solve_captcha("B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",  "https://signup.live.com/?lic=1", "https://client-api.arkoselabs.com",blob, getua(driver), proxy, capsolver_apikey)
    except UnknownError:
        return DETECTED
    except Exception as e:
        traceback.print_exc()
        return DETECTED
    
    submittoken(driver, token)
    captcha_id_before_solved = get_captcha_id(driver)
    driver.switch_to.default_content()


    while driver.is_in_page('signup.live.com'):

        if getphoneverificationelement(driver):
            return PHONE_VERIFICATION
        
        def do():
            try:
                iframe = getiframeelement(driver)  
                if iframe:
                    
                    driver.switch_to.frame(getiframeelement(driver))

                    captcha_id_after_solve = get_captcha_id(driver)

                    if captcha_id_after_solve and captcha_id_after_solve != captcha_id_before_solved:
                        # asking to resolve by giving new captcha given
                        return DETECTED
                    
                    driver.switch_to.default_content()
            except:
              pass
        
        r = do()
        if r:
            return r
        
        time.sleep(1)
    #bt.prompt() 

PHONE_VERIFICATION = 'phone_verification_required'
RETRY = 'RETRY'
DETECTED = 'detected'

def check_for_phone_verification_or_captcha(driver:AntiDetectDriver):
     while True:
          if getiframeelement(driver):
             if getphoneverificationelement(driver):
                return PHONE_VERIFICATION
             else:
                return None   

          if getphoneverificationelementwithwait(driver):
                return PHONE_VERIFICATION


def create_user(proxy):
            country_code = find_ip_details(proxy=proxy)['country']
            number_of_accounts_to_generate =  1
            # config['number_of_accounts_to_generate']
            account = bt.generate_user(number_of_accounts_to_generate, country=country_code)
            account['country'] = country_code
            return account        

def is_bot_detected(driver):
            blocked_el = driver.get_element_or_none_by_text('The request is blocked.', None)
            return blocked_el is not None


def get_unique_cookies(driver:AntiDetectDriver, links):
    unique_cookies = set()

    # Get cookies from the initial page the driver is opened with
    unique_cookies.update({frozenset(cookie.items()) for cookie in driver.get_cookies()})

    # Iterate through each link and collect cookies
    for link in links:
        driver.get(link)
        # time.sleep(5)  # Wait for 5 seconds for the page to load
        cookies = driver.get_cookies()
        
        # Convert each cookie (which is a dictionary) to a frozenset for immutability and then add to the set
        for cookie in cookies:
            unique_cookies.add(frozenset(cookie.items()))

    # Convert the frozensets back to dictionaries
    unique_cookies_dicts = [dict(cookie) for cookie in unique_cookies]

    return unique_cookies_dicts


def waitforretryorsolved(driver):
        print('')
        print('   __ _ _ _    _                          _       _           ')
        print('  / _(_) | |  (_)                        | |     | |          ')
        print(' | |_ _| | |   _ _ __      ___ __ _ _ __ | |_ ___| |__   __ _ ')
        print(r' |  _| | | |  | | `_ \    / __/ _` | `_ \| __/ __| `_ \ / _` |')
        print(' | | | | | |  | | | | |  | (_| (_| | |_) | || (__| | | | (_| |')
        print(r' |_| |_|_|_|  |_|_| |_|   \___\__,_| .__/ \__\___|_| |_|\__,_|')
        print('                                   | |                        ')
        print('                                   |_|                        ')
        print('')
        print('1. Press "R" to Retry Account Creation')
        print('2. Press "Enter" Once Captcha is Solved')
        ipt = bt.prompt("Your Input: ", )
        if ipt == 'r' or ipt == 'R':
            return RETRY