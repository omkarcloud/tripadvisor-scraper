from itertools import cycle
from typing import List, Optional, Union, Dict, Callable
from .create_accounts import  create_accounts
from .create_accounts_utils import DETECTED, PHONE_VERIFICATION, RETRY
from .send_email import send_emails
from .get_emails import get_emails
from .check import check
from .outlook_utils import get_random_delay, prompt_change_ip
from .back import Back
from botasaurus import *
import time
        
BackObject = Back()

class Outlook:
    """
    Provides Outlook email functionalities including account creation, sending and retrieving emails.
    """
    Back = BackObject 

    @staticmethod
    def create_accounts(count: int = 1, proxies: Union[None, str, List[str]] = None, enable_captcha_solving=False) -> None:
        """
        Creates Outlook email accounts.

        :param count: Number of accounts to be created. Defaults to 1.
        :param proxies: Optional proxy server or list of proxy servers to be used for account creation.
        """
        if isinstance(proxies, str):
            proxies = [proxies]  
            

        createdaccounts = []
        if proxies:
            proxies_cycle = cycle(proxies)


        while len(createdaccounts) < count:
            if proxies:
                proxy = next(proxies_cycle)
                data = {"proxy": proxy}
            else:
                data = {"proxy": None}

            if enable_captcha_solving:
                data['captcha'] = True
            
            account = create_accounts(data)
            
            if account is None:
                pass
            elif account == RETRY:
                pass
            elif account == PHONE_VERIFICATION or account == DETECTED:
                # print in method only
                prompt_change_ip(True)
            else:
                createdaccounts.append(account)
                 
                if not proxies:
                    if len(createdaccounts) > 0 and len(createdaccounts) % 3 == 0:
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
        Outlook.send_emails(username, [{"to": to, "subject": subject, "body": body}], proxy=proxy)

    @staticmethod
    def send_emails(username: str, emails: List[Dict[str, str]], proxy: Optional[str] = None, get_random_delay: Callable = get_random_delay) -> None:
        """
        Sends multiple emails from a specified account.

        :param username: The username of the sender's account.
        :param emails: A list of email data including 'to', 'subject', and 'body'.
        :param proxy: Optional proxy server for sending the emails.
        """
        data ={"username":username, "emails":emails, "get_random_delay": get_random_delay, "proxy":proxy} 
        send_emails(data)
    @staticmethod
    def get_latest_email_for_verification(username: str, received=BackObject.JustNow, proxy: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Retrieves the latest email for verification from the specified account.

        :param username: The username of the account.
        :param received: Time filter for received emails.
        :param proxy: Optional proxy server for retrieving the email.
        :return: A dictionary containing details of the latest email or None if no email is found.
        """
        attempts = 4
        while attempts > 0:
            latest_email = Outlook.get_latest_email(username, received=received, proxy=proxy)
            if latest_email:
                return latest_email
            time.sleep(10)  # Wait for 10 seconds before retrying
            attempts -= 1
        return None

    @staticmethod
    def get_latest_email(username: str, received=None, proxy: Optional[str] = None) -> Dict[str, str]:
        """
        Retrieves the latest email from the specified account.

        :param username: The username of the account.
        :param proxy: Optional proxy server for retrieving the email.
        :return: A dictionary containing details of the latest email.
        """
        email = Outlook.get_emails(username, received=received, max=1, proxy=proxy)
        if len(email) == 0:
            return None
        return email[0]

    @staticmethod
    def get_unread_emails(username: str, received=None, max=None, proxy: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Retrieves unread emails from the specified account. Please note that this method will mark the unread emails as read.

        :param username: The username of the account.
        :param proxy: Optional proxy server for retrieving the emails.
        :return: A list of dictionaries, each containing details of an email.
        """
        data ={"username":username, "received":received, "max":max, "unread": True, "proxy":proxy} 
        return get_emails(data)

    @staticmethod
    def get_emails(username: str, received=None, max=None, proxy: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Retrieves emails from the specified account.

        :param username: The username of the account.
        :param proxy: Optional proxy server for retrieving the emails.
        :return: A list of dictionaries, each containing details of an email.
        """
        data ={"username":username, "received":received, "max":max, "unread" :None, "proxy":proxy} 
        return get_emails(data)


    @staticmethod
    def check(username: str, proxy: Optional[str] = None) -> None:
        """
        Allows manual checking of emails for a given account.

        :param username: The username of the account to check.
        """
        data = {"username":username, "proxy":proxy} 
        check(data)

