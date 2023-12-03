![Outlook Account Generator Demo](https://raw.githubusercontent.com/outlook-account-generator/master/images/outlook-account-generator-demo.gif)


<div align="center" style="margin-top: 0;">
  <h1>🚀 Outlook Account Generator 📧</h1>
  <p>💦 Enjoy the Rain of Outlook Accounts 💦</p>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="outlook-account-generator forks" src="https://img.shields.io/github/forks/omkarcloud/outlook-account-generator?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/outlook-account-generator?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="outlook-account-generator License" src="https://img.shields.io/github/license/omkarcloud/outlook-account-generator?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/outlook-account-generator/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/outlook-account-generator?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/outlook-account-generator.svg" width="80px" height="28px" alt="View" />
</p>

---

⚡ Create Unlimited Accounts for Free! ⚡

👋 Hello, I am the Outlook Account Generator, a powerful tool designed to automate the process of creating Outlook email accounts. 

Whether you're a business owner needing multiple accounts for your team, or an individual seeking a hassle-free way to manage various online identities, I've got you covered!

If you've experienced disappointments with other outlook account generator bots, facing failures, crashes and detection from Microsoft, don't worry! Your search for a reliable Outlook Account Generator Bot ends right here ⬇️.

Below is an example of what the created Outlook Account looks like:

![sample profile](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/sample-profile.png)

## ⚡ Features and Benefits

1. **Unlimited Outlook Accounts for Free:** Say goodbye to buying accounts at high prices.
2. **Realistic Account Names:** Accounts are created with human-like names, reducing the chances of getting banned.
3. **Easy Email Sending and Receiving:** *Send* and *receive emails* with just one line of code.
4. **Automatic Captcha Solving:** Save Time and Effort with Automatic Captcha Solving

Ready to Rock n Roll? Let's get started!

## 🎥 Demo

Watch this video to see the bot in action!


[![Outlook Account Generator](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/youtube-video.png)](https://www.youtube.com/watch?v=RwCWcaKBahI)

## 🚀 Getting Started

1️⃣ **Clone the Magic 🧙‍♀:**
   ```shell
   git clone https://github.com/omkarcloud/outlook-account-generator
   cd outlook-account-generator
   ```
2️⃣ **Install Dependencies 📦:**
   ```shell
   python -m pip install -r requirements.txt
   ```
3️⃣ **Let the Rain of Outlook Accounts Begin 😎:**
   ```shell
   python main.py
   ```

The bot will take care of filling in the required details automatically. You will only be prompted to solve the captcha manually.

![solve captcha](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/solve-captcha.png)

Note:
  1. Accounts will be saved in `profiles.json`.
  ![Outlook Account](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/profiles.png)

  2. This Bot requires Firefox, as firefox is able to bypass Microsoft's Anti-Detection Measures. If you don't have Firefox, download it from the Mozilla website [here](https://www.mozilla.org/en-US/firefox/new/).
  

## 🤔 FAQs

### ❓ How to Change the Number of Accounts to Create?
By default, the bot creates 1 account.

To create more accounts, open the `main.py` file and update `Outlook.create_accounts` by adding the `count` parameter. 

This parameter specifies the number of accounts to be created:

```python
Outlook.create_accounts(count=3)
```

The above code will create 3 accounts.

### ❓ How Many Accounts Can I Create?
The sky's the limit! However, Outlook will prompt you for phone verification after every 3 accounts.

![Photo Verification](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/phone-verification.png)


But don't worry! Bypassing the photo verification prompt is very easy. All you need to do is change your IP address.

While there are numerous ways to change your IP, such as using VPNs and proxies, we'll share with you the **fastest**, **simplest**, and best of all, the **free** way which is as follows:

1. **Connect your PC to the Internet via a Mobile Hotspot.**
2. **Toggle airplane mode off and on on your mobile device.** This will assign you a new IP address.
3. **Turn the hotspot back on.**

Please note that you need to repeat this process after every 3 accounts. We will automatically prompt you with a beep sound when it's needed like so.

![Prompt Image](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/prompt-image.png)

### ❓ Can We Solve Captchas Automatically, as Manually Solving Them Is Really Exhausting?

Yes, you can use Captcha Solvers like CapSolver to automatically solve captchas, saving yourself time and effort.

![Captcha Solved](https://raw.githubusercontent.com/outlook-account-generator/master/images/outlook-account-generator-demo.gif)

To set up automatic Captcha solving, follow these steps:

1. Create a CapSolver account at [capsolver.com](https://dashboard.capsolver.com/passport/register).

  ![Sign Up](https://raw.githubusercontent.com/outlook-account-generator/master/images/captcha-sign-up.png)

2. Add funds to your CapSolver account using PayPal, cryptocurrencies, or other payment methods. Note that the minimum deposit is $6, and additional taxes (around 12% for most countries) will apply.

  ![Add Funds](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/add-funds.gif)

3. Copy your API Key.

  ![Store API Key](https://raw.githubusercontent.com/omkarcloud/puppeter-captcha-solving-tutorial/master/images/store-api-key.png)

4. Pass the API Key to `Outlook.create_accounts`:

   ```python
   Outlook.create_accounts(key="CAP-MY_KEY")
   ```

5. Now, Run `python main.py` and the captchas will be automatically solved.

  ![Captcha Solved](https://raw.githubusercontent.com/outlook-account-generator/master/images/outlook-account-generator-demo.gif)

The bot, when provided with a CapSolver key, will run upto 3 accounts in parallel. We limit running accounts to a maximum of 3 in parallel, as running more leads to detection.

---

Also, Special thanks to [Diego](https://github.com/diegoooooooooooooooo) for integrating Captcha Solving functionality, saving all of us time and effort 😌.


### ❓ How to View All Created Accounts?

You can view the accounts you have created in **`profiles.json`**.

![Outlook Account](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/profiles.png)

Additionally, you can get a list of all created accounts by using `Outlook.get_accounts`:
```python
accounts = Outlook.get_accounts()
print(accounts)
```

### ❓ How to Get the Latest Received Email?

To get emails, you need first have some emails in your inbox.

So, Start by sending an email from your personal email to one of the accounts you created, which will have an address like `username@outlook.com`. 

```shell
To: username@outlook.com
Subject: Agenda for Team Meeting
Body: What is the agenda for the upcoming meeting on Monday?
```

After sending the email,

Use the `Outlook.get_latest_email` method as follows:

```python
username = "username123"
Outlook.get_latest_email(username)
```

Printing and viewing emails in the console is cumbersome. So, we create `output/emails.json` containing the emails. Please open `output/emails.json` to view the emails.

Also, your emails will be displayed in a format similar to this:
![sample email](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/sample-email.png)

### ❓ How to Get the Email Verification Link When Using Outlook Accounts to Create Accounts on Other Websites?

When creating accounts on other websites using Outlook accounts, you might not always receive the verification email with `Outlook.get_latest_email`.

This is because verification emails can take anywhere from 10 seconds to 1 minute to arrive.

For such cases, it is recommended to use the `Outlook.get_latest_email_for_verification` method. This smart method performs multiple reloads to retrieve the verification email.

Using `Outlook.get_latest_email_for_verification` significantly increases the reliability of obtaining recently arrived verification emails.

Here's how to use `Outlook.get_latest_email_for_verification`:

```python
username = "username123"
Outlook.get_latest_email_for_verification(username)
```


### ❓ How to get all Emails?

Use `Outlook.get_emails` to get all the emails:

```python
username = "username123" 
Outlook.get_emails(username)
```

### How to Use Outlook Accounts to Sign Up on Other Websites?

In the following section, we will guide you through creating multiple accounts on the Omkar Cloud website with email verification, using Outlook Accounts.

![sign up bot running](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/sign-up-bot-running.gif)

We will use the Botasaurus Framework for this Guide. 

Botasaurus is a Selenium-based bot development framework with anti-detection, temporary emails, user generation, and parallelization capabilities.

**Please note:** To use Outlook Accounts for signing up on other websites, you need first learn Botasaurus, which can be learned easily in about 20 minutes.

Follow these steps to use Outlook accounts for signing up on other websites:

1. Learn about Botasaurus [here](https://github.com/omkarcloud/botasaurus). Botasaurus is a bot development framework designed to save you hours of bot development time.
  
2. Read the Sign Up Tutorial [here](https://www.omkar.cloud/botasaurus/docs/sign-up-tutorial/) to understand how to create sign-up bots with Botasaurus.
   
3. After learning Botasaurus, create a new file in the `src` directory of `outlook-account-generator` and name it `omkar.py`. 

Copy the following code into it, which creates an account on the Omkar Cloud website:
```python

from botasaurus import *
from .outlook import Outlook

@browser(
    data=Outlook.get_accounts()[:1],  # Use only one account for this example
    block_images=True,
    profile=lambda account: account['username'],
    tiny_profile=True,
    output=None
)
def create_omkar_accounts(driver: AntiDetectDriver, account):
    print(bt.Profile.check_profile())
    name = account['name']
    email = account['email']
    username = account['username']
    password = account['password']
    username = account['username']

    def sign_up():
        driver.type('input[name="name"]', name)
        driver.type('input[type="email"]', email)
        driver.type('input[type="password"]', password)
        driver.click('button[type="submit"]')

    def confirm_email():
        
        verification_email = Outlook.get_latest_email_for_verification(username)
        link = verification_email['links'][0]
        driver.get(link)

    driver.organic_get("https://www.omkar.cloud/auth/sign-up/")
    sign_up()
    confirm_email()
    driver.save_screenshot(username)
    bt.Profile.set_profile(account)
```

4. In the `main.py` file, paste the following code to accounts on omkar.cloud :

```python
from src.omkar import create_omkar_accounts

create_omkar_accounts()
```

5. Run the bot using the following command:

```shell
python main.py
```

You will see accounts being created and emails verified. Screenshots after account creation will be saved in the `output` folder.

![sign up bot running](https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/sign-up-bot-running.gif)

---

To make your life even easier, we have created a template for using creating Outlook Accounts to Sign Up on Other Websites, which you can find  [here](https://github.com/omkarcloud/multiple-account-generation-template/blob/master/src/sign_up.py). This template will save you hours of bot development time.

**Important:** Make sure to use proxies with `Outlook.get_latest_email_for_verification` to ensure multiple Outlook accounts don't connect from the same IP address and get suspended.

### ❓ The Target Website has a Sign Up with Microsoft Button, Should I use that or Create Account with Email, Password?

It's recommended to sign up on websites using your email and password rather than using the 'Sign Up with Microsoft' button. 

![email signup withmsft](https://raw.githubusercontent.com/omkarcloud/outlook-account-generator/master/images/email-signup-withmsft.png)

This is because some websites checks your account creation date. If it's too new, they might block your sign-up. 

By manually entering your email and password, the website won't know your account's creation date, reducing the chance of getting blocked.

However, If you must use `Sign Up with Microsoft` and face a block due to a recently created account, wait for about 7 days to let your account get older, and then try again.


### ❓ How to Get Emails Received 1 Day/1 Week Ago?

To get emails a specific timeframe ago, use the `received` parameter.

For example, to get emails received 1 week ago, use the following code:

```python
username = "username123"
ago = Outlook.Ago.OneWeekAgo
Outlook.get_emails(username, received=ago)

```

Some popular options for the `received` parameter are:
- Outlook.Ago.TwoMinutesAgo
- Outlook.Ago.OneHourAgo
- Outlook.Ago.OneDayAgo
- Outlook.Ago.OneWeekAgo
- Outlook.Ago.OneMonthAgo
- Outlook.Ago.OneYearAgo

See the list of all supported timeframes [here](https://github.com/omkarcloud/outlook-account-generator/blob/master/agos.md)

### ❓ How to Send Email?

To send an email, you can use the `Outlook.send_email` method. Replace the `to` with your personal email.

```python
username = "username123"

to = "my-email@gmail.com" # For testing, replace with your personal email
subject = "Product Roadmap Discussion"
body = "We will discuss the product roadmap."

Outlook.send_email(username, to, subject, body)
```

After executing this, check your personal email *primary*/*spam* box to see the sent message.

You can also send emails with HTML content. The following example shows how to send an email with a hyperlink embedded in the body:

```python
username = "username123"

to = "my-email@gmail.com" # For testing, replace with your own email
subject = "Meeting Productivity Article"

body = """I recommend reading <a href='https://www.atlassian.com/work-management/project-collaboration/team-meetings'>this article</a> about improving meeting productivity."""

Outlook.send_email(username, to, subject, body)
```

### ❓ How to Send Multiple Emails with It?

To send multiple emails, use the `Outlook.send_emails` method as follows:

```python
username = "username123"

emails = [
  {
    "to": "my-email@gmail.com",
    "subject": "Presentation Preparation",
    "body": "Have you prepared your presentation?"
  },
  {
    "to": "my-email2@gmail.com",
    "subject": "Rescheduled Meeting",
    "body": "Our meeting has been rescheduled to Wednesday."
  }
]

Outlook.send_emails(username, emails)
```

This method will automatically insert a random delay between each email to make the sending process appear more human-like and avoid account suspension.

### ❓ How to Manually Open the Outlook Website for an Account?

To manually open the Outlook website for a specific account to review emails, use the `Outlook.open` method as follows:

```python
username = "username123" # Replace with your username found in profiles.json
Outlook.open(username)
```

After running, the specified Outlook account will be open in `outlook.live.com`. You will then be prompted to press Enter once you have finished reviewing your emails.

### ❓ What are Popular Use Cases for Outlook Account Generator?

- **Creating Accounts on Websites:**
  - Use `Outlook.create_accounts` to create outlook accounts.
  - Use `Outlook.get_latest_email_for_verification` for getting verification links.

- **Mass Mailing:**
  - Use `Outlook.create_accounts` to create outlook accounts.
  - Send multiple emails with `Outlook.send_emails`.
  - Get all emails from the last day:
    ```python
    username = "username123"
    ago = Outlook.Ago.OneDayAgo
    Outlook.get_emails(username, received=ago)
    ```

### ❓ What precautions should be followed to avoid getting banned while sending and receiving emails?

1. Use different IP addresses for each email account by using rotating residential proxies. 

Also ensure that the proxy's country matches the account's creation country. 

You can use pass proxies as follows:
```python
Outlook.send_email(username, to=to, subject=subject, body=body, proxy="http://username:password@ip:port")
Outlook.get_latest_email(username, proxy="http://username:password@ip:port")
```
2. Personalize your emails. Include the recipient's name and company in the subject and body.

3. Avoid sending excessive emails from a single account, as this can trigger the phone verification process. Instead distribute the email load across multiple accounts.

### ❓ Do you have any recommendations on how many emails to send per day?

1. Limit to 9 emails per account daily. This allows for approximately 10,800 emails per month with 40 accounts (40 accounts x 9 emails/day x 30 days).

2. If more emails are needed, add extra accounts. For example, to send an additional 1,000 emails per month, create 4 more accounts.

3. For better email deliverability, it's recommended to send fewer emails per account and add more accounts if necessary.

### ❓ Advanced Questions

Having read this page, you have all the knowledge needed to effectively utilize the bot and ensure a never ending supply of outlook accounts.

You may choose to explore the following questions based on your interests:

#### For Technical Usage

1. [How to Get Emails Received After a Certain Date?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-get-emails-received-after-a-certain-date)
2. [How to Get a Maximum of 10 Emails?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-get-a-maximum-of-10-emails)
3. [How to Get Unread Emails?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-get-unread-emails)
4. [How to Get Spam Emails Along with Primary Emails?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-get-spam-emails-along-with-primary-emails)
5. [How to Use Proxies for Account Creation?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-use-proxies-for-account-creation)

#### For Knowledge

1. [Which Proxy Provider to Choose?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-which-proxy-provider-to-choose)
2. [Why did you use Firefox for Account Creation instead of Chrome?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-why-did-you-use-firefox-for-account-creation-instead-of-chrome)
3. [How to Use Captcha Solvers like Capsolver and 2Captcha for Automatically Solving Captchas?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-how-to-use-captcha-solvers-like-capsolver-and-2captcha-for-automatically-solving-captchas)
4. [I am an experienced Web Scraper and can integrate Captcha Solving in Bot, where to start?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-i-am-an-experienced-web-scraper-and-can-integrate-captcha-solving-in-bot-where-to-start)
5. [Is the Tool Safe for Account Creation?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-is-the-tool-safe-for-account-creation)
6. [Can the Tool Be Used for Spam or Malicious Activities?](https://github.com/omkarcloud/outlook-account-generator/blob/master/advanced.md#-can-the-tool-be-used-for-spam-or-malicious-activities)

### ❓ Need More Help or Have Additional Questions?

For further help, ask your question in GitHub Discussions. We'll be happy to help you out.

[![ask github](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/ask-on-github.png)](https://github.com/omkarcloud/outlook-account-generator/discussions)


## Love It? [Star It ⭐!](https://github.com/omkarcloud/outlook-account-generator)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/outlook-account-generator](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=outlook-account-generator)](https://github.com/omkarcloud/outlook-account-generator/stargazers)

## Made with ❤️ using [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)
