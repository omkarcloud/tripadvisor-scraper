from botasaurus import *
from .mail_utils import get_profile, get_proxy

browser_attributes = {
        # "headless":True, 
        "user_agent":bt.UserAgent.HASHED,
        "window_size":bt.WindowSize.HASHED,
        "proxy":get_proxy ,
        "profile":get_profile, 
        "tiny_profile":True, 
        "output":None, 
        "block_images":True
}