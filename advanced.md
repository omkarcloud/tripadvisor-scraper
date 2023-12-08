## 🤔 Advanced Questions

### ❓ How to Get Emails Received After a Certain Date?
To get emails from a certain date onwards, use the `received` parameter. 

For example, to get emails after January 1st, 2023 (UTC):

```python
username = "username123"
after = "2023-01-01"
Outlook.get_emails(username, received=after)
```

### ❓ How to Get a Maximum of 10 Emails?
To limit your email retrieval to 10, use the `max` parameter:

```python
username = "username123"
Outlook.get_emails(username, max=10)
```
This fetches the 10 most recent emails in your inbox.

### ❓ How to Get Unread Emails?
To collect all unread emails, use the `Outlook.get_unread_emails` method:

```python
username = "username123"
unread_emails = Outlook.get_unread_emails(username)
print(unread_emails)
```
Note: This action marks unread emails as read.

### ❓ How to Get Spam Emails Along with Primary Emails?
To get both primary and spam emails, set the `with_spam` parameter to `True`:

```python
username = "username123"
emails = Outlook.get_emails(username, with_spam=True)
print(emails)
```

### ❓ How to Use Proxies for Account Creation?
You may use proxies as follows:

```python
proxies = [
    "http://myusername1:mypassword@myproxy-provider.com:8080",
    "http://myusername2:mypassword@myproxy-provider.com:8080",
]
Outlook.create_accounts(count=4, proxies=proxies)
```
Also, we will rotate the proxies automatically.

### ❓ Which Proxy Provider to Choose?

#### For Account Creation:
Currently, manual account creation is recommended as popular proxies like Bright Data and IPRoyal refuses to connect for signup urls. 

However, if you know of any Proxy Provider that works for creating Outlook Accounts, please let us know in the Github Discussions [here](https://github.com/omkarcloud/outlook-account-generator/discussions), and we will add them to the list. This will help you earn Good Karma.

#### For Getting/Sending Emails:

During our testing, IPRoyal worked well for getting/sending emails. Avoid using Bright Data as it refuses to connect.


### ❓ Why did you use Firefox for Account Creation instead of Chrome?

Chrome was getting detected, and we were facing the following problems:

- Captchas were much harder and longer to solve (10 steps long).
- Even after successfully solving the Captcha, we were asked to solve it again and again in a loop.

So, we used Firefox, which doesn't cause these issues, and Captchas are much easier to solve.

### ❓ I am facing Errors?

If you encounter the error `API Rate limit exceeded. You have to add GH_TOKEN`, which is common in Ubuntu, follow these steps:

1. Get a GitHub Token by following [these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token). Your token will look something like `ghp_3fMk7naX9EypRQlG4jHsUoF6Zc1TbYvW8AeP`. It's a bit tedious I know, but you're just one step away from creating Outlook accounts.
2. Paste the following code into `main.py`. Replace `your_github_token_here` with your GitHub token:
   ```python
   from src import Outlook
   import os

   love_it_star_it = '''Love It? Star It! ⭐ https://github.com/omkarcloud/outlook-account-generator/'''

   os.environ['GH_TOKEN'] = "your_github_token_here"

   Outlook.create_accounts()
   ```
3. Run `python main.py` and you are good to go.

### ❓ Is the Tool Safe for Account Creation?
Absolutely. It's trusted by thousands of developers globally for creating Outlook accounts.

### ❓ Can the Tool Be Used for Spam or Malicious Activities?
No. It's meant for legitimate uses like business, testing, and personal accounts. Misuse for spam or malicious acts is against our and Microsoft's policies.


### ❓ Need More Help or Have Additional Questions?

For further help, ask your question in GitHub Discussions. We'll be happy to help you out.

[![ask github](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/ask-on-github.png)](https://github.com/omkarcloud/outlook-account-generator/discussions)


## Love It? [Star It ⭐!](https://github.com/omkarcloud/outlook-account-generator)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/outlook-account-generator](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=outlook-account-generator)](https://github.com/omkarcloud/outlook-account-generator/stargazers)

## Made with ❤️ using [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)