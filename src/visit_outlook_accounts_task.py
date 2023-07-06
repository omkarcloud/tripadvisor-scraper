from bose import *

class VisitOutlookAccountsTask(BaseTask):
    def get_data(self):
        return Profile.get_profiles(random=True)

    def get_task_config(self):
        return TaskConfig(
            # prompt_to_close_browser=not self.is_new_user(),
            # change_ip=not self.is_new_user(),
        )

    def get_browser_config(self, data):
        return BrowserConfig(
            profile=data['username'],
            is_tiny_profile=True,
        )

    def run(self, driver: BoseDriver, data):
        driver.organic_get('https://account.microsoft.com/')
        driver.prompt()
