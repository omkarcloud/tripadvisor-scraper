from botasaurus.ip_utils import get_valid_ip
from botasaurus.beep_utils import beep_input
from botasaurus.local_storage import LocalStorage
from botasaurus import *
from random import uniform

def get_random_delay():
  return uniform(3, 5) # random delay

#   return uniform(27, 37) # random delay

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
