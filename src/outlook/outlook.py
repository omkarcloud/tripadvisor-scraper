from itertools import cycle
from typing import List, Optional, Union, Dict
from .create_accounts import  create_accounts
from .create_accounts_utils import DETECTED, PHONE_VERIFICATION, RETRY

from botasaurus.ip_utils import get_valid_ip
from botasaurus.beep_utils import beep_input
from botasaurus.local_storage import LocalStorage


def prompt_change_ip(should_beep):
    current_ip = get_valid_ip()
    seen_ips =  LocalStorage.get_item("seen_ips", [])
    
    next_prompt = "Please change your IP and press Enter to continue..."
    
    while True:
        beep_input(next_prompt, should_beep)
        new_ip = get_valid_ip()

        # TODO: url needs to be change to help them learn to change ip.
        if new_ip == current_ip:
            next_prompt = """In order to proceed, it is necessary to change your IP address as a precautionary measure against Bot Detection. Please visit https://github.com/omkarcloud/botasaurus/blob/master/github-docs/change-ip.md to learn how to change your IP. Once you have successfully changed your IP address, please press Enter to continue..."""

        elif new_ip in seen_ips:
            next_prompt = "Your computer previously had this IP address. Please change your IP and press Enter to continue..."
        else:
            LocalStorage.set_item("seen_ips", LocalStorage.get_item("seen_ips", []) + [current_ip])
            return new_ip
        
class Outlook:
    """
    Provides Outlook email functionalities including account creation, sending and retrieving emails.
    """

    @staticmethod
    def create_accounts(count: int = 1, proxies: Union[None, str, List[str]] = None, enable_captcha_solving=False) -> None:
        """
        Creates Outlook email accounts.

        :param count: Number of accounts to be created. Defaults to 1.
        :param proxies: Optional proxy server or list of proxy servers to be used for account creation.
        """
        if isinstance(proxies, str):
            proxies = [proxies]  # Wrap the string in a list
        

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
                # createTempProfile(account)
                createdaccounts.append(account)
                 
                if not proxies:
                    if len(createdaccounts) > 0 and len(createdaccounts) % 2 == 0:
                        prompt_change_ip(True)

        
        return createdaccounts

    @staticmethod
    def get_accounts() -> List[str]:
        """
        Retrieves a list of created Outlook accounts.

        :return: List of accounts
        """
        # Implementation of retrieving accounts
        # Return a list of usernames (dummy data or real data depending on your application)
        return ["username1", "username2"]  # Example return value

    @staticmethod
    def send_email(username: str, to: str, subject: str, body: str, proxy: Optional[str] = None) -> None:
        """
        Sends an email from a specified account.

        :param username: The username of the sender's account.
        :param to: The recipient's email address.
        :param subject: The subject of the email.
        :param body: The body content of the email.
        :param proxy: Optional proxy server for sending the email.
        """
        # Implementation of sending email
        pass

    @staticmethod
    def send_emails(emails: List[Dict[str, str]], username: str, proxy: Optional[str] = None) -> None:
        """
        Sends multiple emails from a specified account.

        :param emails: A list of email data including 'to', 'subject', and 'body'.
        :param username: The username of the sender's account.
        :param proxy: Optional proxy server for sending the emails.
        """
        # Implementation of sending multiple emails
        pass

    @staticmethod
    def get_latest_email(username: str, proxy: Optional[str] = None) -> Dict[str, str]:
        """
        Retrieves the latest email from the specified account.

        :param username: The username of the account.
        :param proxy: Optional proxy server for retrieving the email.
        :return: A dictionary containing details of the latest email.
        """
        # Implementation of retrieving the latest email
        return {"to": "example@example.com", "subject": "Sample Subject", "body": "Sample body"}  # Example return value

    @staticmethod
    def get_emails(username: str, proxy: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Retrieves all emails from the specified account.

        :param username: The username of the account.
        :param proxy: Optional proxy server for retrieving the emails.
        :return: A list of dictionaries, each containing details of an email.
        """
        # Implementation of retrieving all emails
        return [
            {"to": "example@example.com", "subject": "Email 1", "body": "Body of email 1"},
            {"to": "example2@example.com", "subject": "Email 2", "body": "Body of email 2"}
        ]  # Example return value