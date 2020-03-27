# Code by Max Petrov mp7384j
from datetime import datetime


class TimerDate:
    def __init__(self):
        self.election_period = False

    def within_election_period(self):
        """Method checks whether it is the current voting window"""
        today_date = datetime.today()
        print("Today's date:", today_date)

        # Time and date that the election window ends
        end_date = datetime(2020, 1, 27, 22)
        # Set this datetime to the beginning of the election period
        start_date = today_date


        if today_date <= end_date >= start_date:
            self.election_period = True
            return self.election_period
        else:
            return self.election_period