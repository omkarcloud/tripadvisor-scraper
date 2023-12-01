from botasaurus.ip_utils import get_valid_ip
from botasaurus.beep_utils import beep_input
from botasaurus.local_storage import LocalStorage
from botasaurus import *
from random import uniform

def get_random_delay():
  return uniform(3, 5) # random delay


def prompt_change_ip(should_beep):
    current_ip = get_valid_ip()
    seen_ips =  LocalStorage.get_item("seen_ips", [])
    
    
    next_prompt = "Microsoft allows a maximum of 3 accounts per IP address. To create more accounts, kindly change your IP and press Enter to continue..."
    
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

def prompt_change_ip3(should_beep):
    current_ip = get_valid_ip()
    seen_ips =  LocalStorage.get_item("seen_ips", [])
    
    
    next_prompt = "The Bot has been detected. To create more accounts, kindly change your IP and press Enter to continue..."
    
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


def prompt_change_ip2(should_beep, user):
    current_ip = get_valid_ip()
    seen_ips =  LocalStorage.get_item("seen_ips", [])
    
    next_prompt = f"{user}, previously used this IP. To avoid Microsoft phone verification, Kindly change your IP and press Enter to continue..."
    
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


def clean_username(username):
    return username if "@" not in username else username.split("@")[0]

def ensure_unique_ip(username):
    """
    Confirms that no two users have the same IP.

    Args:
    username (str): The username to check the IP against.
    ip (str): The IP address to be checked.

    Returns:
    bool: True if the IP is unique to the user, False otherwise.
    """
    ip = get_valid_ip()
    ip_user_mapping = LocalStorage.get_item("ip_user_mapping", {})

    # Check if the IP exists in the mapping and if it's associated with a different user
    if ip in ip_user_mapping and ip_user_mapping[ip] != username:
        prompt_change_ip2(True, ip_user_mapping[ip])
        return False

    # Update the mapping with the new user-IP association
    ip_user_mapping[ip] = username
    LocalStorage.set_item("ip_user_mapping", ip_user_mapping)
    return True
