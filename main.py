from src import Outlook

love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/outlook-account-generator/'''

#add your CAPSOLVER_API_KEY here if enable_captcha_solving=True

Outlook.create_accounts(enable_captcha_solving=False, capsolver_apikey="CAPSOLVER_API_KEY")