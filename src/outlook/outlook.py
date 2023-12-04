from itertools import cycle
from typing import List, Optional, Union, Dict, Callable

from src.outlook.browser_attributes import set_headless
from .create_accounts import  create_accounts
from .create_accounts_utils import DETECTED, PHONE_VERIFICATION, RETRY
from .send_email import send_emails
from .get_emails import get_emails
from .check import check
from .outlook_utils import clean_username, get_random_delay, prompt_change_ip, ensure_unique_ip, prompt_change_ip3
from .ago import Ago
from botasaurus import *
import time
        
AgoObject = Ago()

class Outlook:
    """
    Provides Outlook email functionalities including account creation, sending and retrieving emails.
    """
    Ago = AgoObject 

    @staticmethod
    def create_accounts(count: int = 1, key=None, proxies: Union[None, str, List[str]] = None, ) -> None:
        """
        Creates Outlook email accounts.

        :param count: Number of accounts to be created. Defaults to 1.
        :param key: Capsolver Api Key for solving captchas automatically. Defaults to None.
        :param proxies: Optional proxy server or list of proxy servers to be used for account creation.
        """
        if isinstance(proxies, str):
            proxies = [proxies]  
            
        if proxies:
            proxies_cycle = cycle(proxies)

        def create_data(key):
            nonlocal proxies_cycle
            if proxies:
                proxy = next(proxies_cycle)
                data = {"proxy": proxy}
            else:
                data = {"proxy": None}

            if key:
                data['captcha'] = True
                data['capsolver_apikey'] = key
            else:
                data['captcha'] = False
                data['capsolver_apikey'] = None

            return data            

        createdaccounts = []

        MICROSOFT_ACCOUNT_CREATION_LIMIT = 3
        
        if key:
            if not proxies:
                parallel = MICROSOFT_ACCOUNT_CREATION_LIMIT
            else:
                parallel = bt.calc_max_parallel_browsers(min=MICROSOFT_ACCOUNT_CREATION_LIMIT)

            while len(createdaccounts) < count:


                if not proxies:
                    tobecreated =  min(parallel,  count - len(createdaccounts))
                else:
                    tobecreated =  count - len(createdaccounts)

                temp =  [None] *  tobecreated
                ls = [create_data(key) for i in temp]

                ctd = create_accounts(ls, parallel = parallel)
                
                pmt = prompt_change_ip
                for i in ctd:
                    if type(i) is dict:
                        createdaccounts.append(i)        
                    if i == PHONE_VERIFICATION or i == DETECTED:
                        pmt = prompt_change_ip3
                
                if not proxies:
                    if len(createdaccounts) < count:
                        pmt(True)

            return createdaccounts

        else:
            rantimes = 0
            while len(createdaccounts) < count:
                data = create_data(key)

                account = create_accounts(data)
                rantimes+=1   
                if account is None:
                    pass
                elif account == RETRY:
                    pass
                elif account == PHONE_VERIFICATION or account == DETECTED:
                    # print in method only

                    if len(createdaccounts) < count:
                        prompt_change_ip3(True)
                else:
                    createdaccounts.append(account)
                    
                    if not proxies:
                        if rantimes==MICROSOFT_ACCOUNT_CREATION_LIMIT:
                            rantimes=0
                            if len(createdaccounts) < count:
                                prompt_change_ip(True)

        
            return createdaccounts

    @staticmethod
    def get_accounts() -> List[str]:
        """
        Retrieves a list of created Outlook accounts.

        :return: List of accounts
        """
        
        return bt.Profile.get_profiles()


    @staticmethod
    def get_account_usernames() -> List[str]:
        """
        Retrieves a list of created Outlook accounts usernames.

        :return: List of accounts
        """
        
        return [account['username'] for account in Outlook.get_accounts()]

    @staticmethod
    def send_email(username: str, to: str, subject:Optional[str], body: str, proxy: Optional[str] = None ) -> None:
        """
        Sends an email from a specified account.

        :param username: The username of the sender's account.
        :param to: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :param proxy: Optional proxy server for sending the email.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        Outlook.send_emails(username, [{"to": to, "subject": subject, "body": body}], proxy=proxy)

    @staticmethod
    def send_emails(username: str, emails: List[Dict[str, str]], proxy: Optional[str] = None, get_random_delay: Callable = get_random_delay) -> None:
        """
        Sends multiple emails from a specified account.

        :param username: The username of the sender's account.
        :param emails: A list of email data including 'to', 'subject', and 'body'.
        :param proxy: Optional proxy server for sending the emails.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        data ={"username":username, "emails":emails, "get_random_delay": get_random_delay, "proxy":proxy} 
        send_emails(data)
    @staticmethod
    def get_latest_email_for_verification(username: str, received=AgoObject.JustNow, with_spam=True, exclude_outlook_team_emails=True, proxy: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Retrieves the latest email for verification from the specified account.

        :param username: The username of the account. (str)
        :param received: Time filter for received emails, can be datetime, timedelta or string. Default is JustNow. (recieved 2 minutes ago)
        :param with_spam: Include spam emails. Default is True. (bool)
        :param exclude_outlook_team_emails: Whether to exclude emails from Outlook team. Default is True. (bool)
        :param proxy: Optional proxy server for retrieving the email. (str, optional)
        :return: A dictionary containing details of the latest email or None if no email is found.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        attempts = 4
        while attempts > 0:
            latest_email = Outlook.get_latest_email(username, received=received, with_spam=with_spam, exclude_outlook_team_emails=exclude_outlook_team_emails, proxy=proxy)
            if latest_email:
                return latest_email
            time.sleep(10)  # Wait for 10 seconds before retrying
            attempts -= 1
        return None

    @staticmethod
    def get_latest_email(username: str, received=None, with_spam=False, exclude_outlook_team_emails=False, proxy: Optional[str] = None) -> Dict[str, str]:
        """
        Retrieves the latest email from the specified account.

        :param username: The username of the account. (str)
        :param received: Time filter for received emails. Default is None meaning No Filters. (Ago or None)
        :param with_spam: Include spam emails. Default is False. (bool)
        :param exclude_outlook_team_emails: Whether to exclude emails from Outlook team. Default is False. (bool)
        :param proxy: Optional proxy server for retrieving the email. (str, optional)
        :return: A dictionary containing details of the latest email.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        email = Outlook.get_emails(username, received=received, with_spam=with_spam, exclude_outlook_team_emails=exclude_outlook_team_emails, max=1, proxy=proxy)
        if len(email) == 0:
            return None
        return email[0]

    @staticmethod
    def get_unread_emails(username: str, received=None, max=None, with_spam=False, exclude_outlook_team_emails=False, proxy: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Retrieves unread emails from the specified account. Please note that this method will mark the unread emails as read.

        :param username: The username of the account. (str)
        :param received: Time filter for received emails. Default is None meaning No Filters. (Ago or None)
        :param max: Maximum number of emails to retrieve. Default is None. (int or None)
        :param with_spam: Include spam emails. Default is False. (bool)
        :param exclude_outlook_team_emails: Whether to exclude emails from Outlook team. Default is False. (bool)
        :param proxy: Optional proxy server for retrieving the emails. (str, optional)
        :return: A list of dictionaries, each containing details of an email.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        data = {"username": username, "received": received, "max": max, "unread": True, "with_spam": with_spam, "exclude_outlook_team_emails": exclude_outlook_team_emails, "proxy": proxy}
        return get_emails(data)

    @staticmethod
    def get_emails(username: str, received=None, max=None, with_spam=False, exclude_outlook_team_emails=False, proxy: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Retrieves emails from the specified account.

        :param username: The username of the account. (str)
        :param received: Time filter for received emails. Default is None meaning No Filters. (Ago or None)
        :param max: Maximum number of emails to retrieve. Default is None. (int or None)
        :param with_spam: Include spam emails. Default is False. (bool)
        :param exclude_outlook_team_emails: Whether to exclude emails from Outlook team. Default is False. (bool)
        :param proxy: Optional proxy server for retrieving the emails. (str, optional)
        :return: A list of dictionaries, each containing details of an email.
        """
        username = clean_username(username)
        if not proxy:
            ensure_unique_ip(username)
        data = {"username": username, "received": received, "max": max, "unread": None, "with_spam": with_spam, "exclude_outlook_team_emails": exclude_outlook_team_emails, "proxy": proxy}
        return get_emails(data)


    @staticmethod
    def open(username: str, proxy: Optional[str] = None) -> None:
        """
        Allows manually opening outlook for a given account.

        :param username: The username of the account to check.
        :param proxy: Optional proxy server for opening Outlook. (str, optional)
        """
        username = clean_username(username)
        
        if not proxy:
            ensure_unique_ip(username)
        data = {"username":username, "proxy":proxy} 
        check(data)

    @staticmethod
    def show_in_action() -> None:
        """
        Shows Browser when sending recieving emails.
        """
        
        set_headless(False)


    @staticmethod
    def disable_show_in_action() -> None:
        """
        Hides Browser when sending recieving emails.
        """
        
        set_headless(True)



    