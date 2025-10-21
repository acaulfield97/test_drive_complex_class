from datetime import datetime, timedelta

class Birthday:

    def __init__(self):
        self.birthdays = {}

    def add_record(self, name, birthday):
        self.birthdays[name] = birthday

    def get_record(self, name):
        return self.birthdays.get(name)

    def update_birthday(self, name, updated_birthday):
        self.birthdays[name] = updated_birthday

    def edit_name(self, name, new_name):
        self.birthdays[new_name] = self.birthdays.pop(name)

    def birthday_reminder(self):
        today = datetime.today()
        next_7_days = []
        reminders = []

        for i in range(7):
            future_date = today + timedelta(days=i) # add i days to today
            day_month = future_date.strftime("%d-%m")
            next_7_days.append(day_month)

        for name, birthday_str in self.birthdays.items():
            birthday = datetime.strptime(birthday_str, "%d-%m-%Y")
            birthday_day_month = birthday.strftime("%d-%m")
            if birthday_day_month in next_7_days:
                reminders.append(name)

        return reminders



