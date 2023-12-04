from .browser_attributes import browser_attributes
from botasaurus import *
from datetime import datetime, timezone, timedelta
from time import time, sleep
from .enrich_email import enrich_email 
from .mail_utils import  load_outlook, open_junk_mail 
from botasaurus.decorator_helpers import retry_on_stale_element
def convert_to_utc(time_str):
    # Parse the string to a datetime object
    
    try:
        local_time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S%z')
    except ValueError:
        local_time = datetime.strptime(time_str, '%Y-%m-%d')
        dt_utc = local_time.replace(tzinfo=timezone.utc)
        return dt_utc

    # Convert to UTC
    utc_time = local_time.astimezone(timezone.utc)

    return utc_time

def toiso(date):
    return date.isoformat() 

def perform_get_emails(driver:AntiDetectDriver, received=None, max=None, is_unread=None, exclude_outlook_team_emails=True):

    def is_received_date_before_now(received_date_str, now_utc=None, ):
        # Parse the received_date string into a datetime object
        received_date = convert_to_utc(received_date_str)

        # Compare and return the result
        return received_date < now_utc


    def getspinner():
        return driver.get_element_or_none_by_selector("#MailList .customScrollBar .ms-Spinner ", 2 )


    @retry_on_stale_element
    def getcons():
        els = getconsels()
        if els:
            return els, [el.get_attribute("data-convid") for el in els]
        else:
            return [], []

    def getconsels():
        return driver.get_elements_or_none_by_selector("#MailList .customScrollBar [data-convid]", bt.Wait.SHORT )
    
    def hasscrolledtoend():
        el = driver.get_element_or_none_by_selector('#MailList .customScrollBar', bt.Wait.SHORT )
        return not driver.can_element_be_scrolled(el)

    seen_conversations = set()

    @retry_on_stale_element()
    def get_new_links():
        nonlocal seen_conversations

        new_items = []
        while True:
            
            consels, cons  = getcons()
            
            for con in cons:
                if con not in seen_conversations:
                    new_items.append(con)
                    seen_conversations.add(con)
            
            if new_items:
                return new_items
            
            if not cons:
                # no emails
                return []
            
            driver.scroll_into_view(consels[-1])

            while getspinner():
                sleep(1)

            if hasscrolledtoend() and not getspinner():
                consels, cons  = getcons()
                
                for con in cons:
                    if con not in seen_conversations:
                        new_items.append(con)
                        seen_conversations.add(con)

                return new_items



    def sort_dict_by_keys(dictionary, keys):
        new_dict = {}
        for key in keys:
            dictkey = key[0]
            newdictkey = key[1]

            try:
                new_dict[newdictkey] = dictionary[dictkey]
            except KeyError:
                pass
        return new_dict


    
    def get_email_details(convids):
        es =  driver.execute_script("return window.getEmails(arguments[0])", convids)

        keys = [
            ["email_id",   "id"],
            ["email_subject",   "subject"],
            ["email_body_text",   "body_plain_text"],
            ["email_links",   "links"],
            ["sender",   "from"],
            ["received_date",   "received_at"],
            ["read",   "is_read"],
            ["email_verification_link",   "verification_link"],
            ["email_otp",   "otp_code"],
            ["is_draft",   "is_draft"],
            ["to",   "recipients"],
            ["replies",   "reply_messages"],
            ["attachments",   "attachments"],
            ["email_body_format",   "body_format"],
            ["email_body_content",   "body_content"],
        ]

        attachments_keys = [
            ["attachment_id", "attachment_id"],
            ["name", "name"],
            ["content_id", "content_id"],
            ["content_type", "content_type"],
            ["size", "size"],
            ["last_modified_time", "last_modified_time"],
        ]

        for e in es:
            for repl in e['replies']:
                repl['received_date'] = toiso(convert_to_utc(repl['received_date']))
                repl['attachments'] = [sort_dict_by_keys(at, attachments_keys) for at in repl['attachments']]    
            
            e['received_date'] = toiso(convert_to_utc(e['received_date']))
            e['attachments'] = [sort_dict_by_keys(at, attachments_keys) for at in e['attachments']]    
            e['replies'] = [sort_dict_by_keys( enrich_email(repl) , keys) for repl in e['replies']]    

        rst = [sort_dict_by_keys(enrich_email(e), keys) for e in es]   

        return rst

    def exec_get_email(convid):
        return driver.execute_script("return window.getEmail(arguments[0])", convid)
    
    def is_received_date_before_now_for_email(received, email_detail):
        before_now =  is_received_date_before_now(email_detail['received_date'],  received)

        if before_now:
            for repl in email_detail['replies']:
                rst = is_received_date_before_now(repl['received_date'],  received)
                if rst:
                    pass
                else:
                    before_now = rst
                    break

        return before_now

    def get_email_detail(convid):
        nonlocal seen_conversations

        start_time = time()
                
        WAIT_TIME = 20 # WAIT 40 SECONDS

        while True:
            # Execute JavaScript to get all emails
            em = exec_get_email(convid)
            if em:
                return em
            driver.click(f'#MailList .customScrollBar [data-convid="{convid}"]')
            sleep(0.3) 

            elapsed_time = time() - start_time
            if elapsed_time > WAIT_TIME :

        # can raise exception which will be caught by the caller and all be redone
        # seen > 18                
                is_first_page = len(seen_conversations) < 18
                print(is_first_page, f"waited {elapsed_time} seconds for email {convid} to load")
                WAIT_TIME = WAIT_TIME + 20
                # TODO: raise later
                    # IF ANY CASE PRINTED
                    # ELSE REMOVE
                
    convs = get_new_links()

    result = []
    while convs and (max is None or len(result) < max):
        conv = convs.pop(0)

        email_detail = get_email_detail(conv)
        is_outlook_email = "Outlook" in email_detail['sender']["name"]
        if is_outlook_email and exclude_outlook_team_emails:
            pass
        else:
            if received and is_received_date_before_now_for_email(received, email_detail):
                break
            
            if is_unread is not None:
                    isemail_unread = not email_detail['read']
                    
                    if is_unread == (isemail_unread):
                        result.append(conv)      
                    else:
                        replies = email_detail['replies']
                        for repl in replies:
                            if is_unread == (not repl['read']):
                                result.append(conv)
                                break
            else:
                result.append(conv)
         
        if len(convs) == 1:
            new_links = get_new_links()

            for new_link in new_links:
                convs.append(new_link)

    if max is not None:
        result = result[:max]

    fnl = get_email_details(result)
     
    return fnl


def get_now_utc(data):
    delta = data
    
    if delta is None:
        now_utc = None
    elif isinstance(delta, timedelta):
        now_utc = datetime.now(timezone.utc) - delta
    elif isinstance(delta, datetime):
        now_utc = delta
    elif isinstance(delta, str):
        now_utc = convert_to_utc(delta)
    else:
        now_utc = delta
    return now_utc


@browser(
        **browser_attributes,
        output="emails", 
        is_eager=True, # This Is Important, because we must start email spying before anything is loaded
)
def get_emails(driver:AntiDetectDriver, data):
    
    now_utc = get_now_utc(data['received'])
    username = data['username']
    load_outlook(driver, username, spy_emails=True)
    
    unread = data['unread']
    with_spam = data['with_spam']
    exclude_outlook_team_emails = data['exclude_outlook_team_emails']

    # els = []

    els  = perform_get_emails(driver, received=now_utc, max=data['max'], is_unread=unread, exclude_outlook_team_emails=exclude_outlook_team_emails)    

    if with_spam:
        mx = data['max']
        if mx is not None:
            mx = mx - len(els)

        open_junk_mail(driver, username, spy_emails=True)

        els  = els + perform_get_emails(driver, received=now_utc, max=mx, is_unread=unread,exclude_outlook_team_emails=exclude_outlook_team_emails)    
    return els
