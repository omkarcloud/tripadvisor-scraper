from botasaurus import *
from .mail_utils import get_profile, get_proxy

headless = False
def get_headless(_):
    global headless
    return headless

def set_headless(val):
    global headless
    headless = val

browser_attributes = {
        "headless":get_headless, 
        "user_agent":bt.UserAgent.HASHED,
        "window_size":bt.WindowSize.HASHED,
        "proxy":get_proxy ,
        "profile":get_profile, 
        "tiny_profile":True, 
        # "output":None, 
        "block_images":True
}