from datetime import timedelta

class Back:

    @property
    def JustNow(self):
        return timedelta(minutes=2)

    @property
    def OneMinuteBack(self):
        return timedelta(minutes=1)

    @property
    def TwoMinutesBack(self):
        return timedelta(minutes=2)

    @property
    def FiveMinutesBack(self):
        return timedelta(minutes=5)

    @property
    def TenMinutesBack(self):
        return timedelta(minutes=10)

    @property
    def OneHourBack(self):
        return timedelta(hours=1)

    @property
    def OneDayBack(self):
        return timedelta(days=1)

    @property
    def TwoDaysBack(self):
        return timedelta(days=2)

    @property
    def OneWeekBack(self):
        return timedelta(weeks=1)

    @property
    def OneMonthBack(self):
        # Roughly approximate a month as 30 days
        return timedelta(days=30)

    @property
    def ThreeMonthsBack(self):
        # Roughly approximate three months as 90 days
        return timedelta(days=90)

    @property
    def SixMonthsBack(self):
        # Roughly approximate six months as 180 days
        return timedelta(days=180)

    @property
    def OneYearBack(self):
        # Roughly approximate a year as 365 days
        return timedelta(days=365)

