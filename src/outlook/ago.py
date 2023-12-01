from datetime import timedelta

class Ago:

    @property
    def JustNow(self):
        return timedelta(minutes=2)

    @property
    def OneMinuteAgo(self):
        return timedelta(minutes=1)

    @property
    def TwoMinutesAgo(self):
        return timedelta(minutes=2)

    @property
    def FiveMinutesAgo(self):
        return timedelta(minutes=5)

    @property
    def TenMinutesAgo(self):
        return timedelta(minutes=10)

    @property
    def OneHourAgo(self):
        return timedelta(hours=1)

    @property
    def TwoHourAgo(self):
        return timedelta(hours=2)


    @property
    def ThreeHourAgo(self):
        return timedelta(hours=3)


    @property
    def FourHourAgo(self):
        return timedelta(hours=4)


    @property
    def FiveHourAgo(self):
        return timedelta(hours=5)


    @property
    def SixHourAgo(self):
        return timedelta(hours=6)

    @property
    def OneDayAgo(self):
        return timedelta(days=1)

    @property
    def TwoDaysAgo(self):
        return timedelta(days=2)

    @property
    def OneWeekAgo(self):
        return timedelta(weeks=1)

    @property
    def OneMonthAgo(self):
        # Roughly approximate a month as 30 days
        return timedelta(days=30)

    @property
    def ThreeMonthsAgo(self):
        # Roughly approximate three months as 90 days
        return timedelta(days=90)

    @property
    def SixMonthsAgo(self):
        # Roughly approximate six months as 180 days
        return timedelta(days=180)

    @property
    def OneYearAgo(self):
        # Roughly approximate a year as 365 days
        return timedelta(days=365)

