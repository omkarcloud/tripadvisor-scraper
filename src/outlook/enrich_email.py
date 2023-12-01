from bs4 import BeautifulSoup
import re
from unidecode import unidecode

def unicode_to_ascii(text):
    """
    Convert unicode text to ASCII, replacing special characters.
    """
    # Replacing 'ë' with 'e' and return the ASCII text
    return unidecode(text).replace("ë", "e")


def unique_strings(lst):
    # Use a set to remove duplicates, then convert back to a list
    return list(dict.fromkeys(lst))

def sort_links(links):
    return sorted(links, key=lambda l: any(token in l for token in ['token', 'verify', 'pass', 'reset']), reverse=True)

def enrich_email(email):
    email_body = email['email_body_content']
    body_type = email['email_body_format']

    if body_type.upper() == 'HTML'.upper():
        # Parse HTML to extract text and links
        soup = BeautifulSoup(email_body, 'html.parser')
        email_body_text = unicode_to_ascii(soup.get_text().strip()).strip()
        links = [a['href'] for a in soup.find_all('a', href=True)]
#      body_type == 'TEXT'
    else:
        # For plain text, the body is used as is
        email_body_text = email_body.strip()
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_body)

    links = unique_strings(links)
    # Add extracted or original email body text
    email['email_body_text'] = email_body_text

    # Sort links to bring verification links to the top
    email['email_links'] = sort_links(links)

    # Finding the verification link
    verification_link = next((link for link in email['email_links'] if any(token in link for token in ['token', 'verify', 'pass', 'reset'])), None)
    email['email_verification_link'] = verification_link

    # Finding any OTPs in the email body
    otps = re.findall(r'\b\d{4,6}\b', email_body_text)
    email["email_otp"] = otps[0] if otps else None

    return email

