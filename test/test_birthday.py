from datetime import datetime
from lib.birthday import Birthday
import pytest

"""
birthdays list is initialised 
"""
def test_initialise_empty_birthday_list():
    birthday = Birthday()
    assert birthday.birthdays == {}

"""
Given a name and a birthday
#add_record adds friends name and birthday to birthdays dictionary
"""
def test_add_name_and_birthday_to_dictionary():
    birthday = Birthday()
    birthday.add_record("Person1", "01-01-2000")
    assert birthday.get_record("Person1") == "01-01-2000"

"""
Given a name and updated birthday
#update_record updates birthdays dictionary with friend's name and new birthday
"""
def test_given_name_and_updated_bday_updates_birthday():
    birthday = Birthday()
    birthday.add_record("Person1", "01-01-2000")
    birthday.update_birthday("Person1", "01-02-2000")
    assert birthday.get_record("Person1") == "01-02-2000"

"""
Given old name and new name
#edit_name changes friend's name to new_name and updates dictionary
"""
def test_edits_name_successfully():
    birthday = Birthday()
    birthday.add_record("Person1", "01-01-2000")
    birthday.edit_name("Person1", "New Person")
    assert "Person1" not in birthday.birthdays
    assert "New Person" in birthday.birthdays

"""
#birthday_reminder returns list of friends birthdays that are in 7 days or less
"""
def test_returns_list_of_birthdays_in_less_than_seven_days():
    birthday = Birthday()
    birthday.add_record("Person1", "01-01-2000")
    birthday.add_record("Person2", "02-02-1990")
    birthday.add_record("Person3", "22-10-2000")
    birthday.add_record("Person4", "26-10-1990")
    assert birthday.birthday_reminder() == ["Person3", "Person4"]

"""
Given a list of friends names and today's date
Returns a new dictionary of friends names and their ages
"""
def test_given_friends_name_and_todays_date_calculate_age():
    birthday = Birthday()
    birthday.add_record("Person1", "11-11-2000") 
    birthday.add_record("Person2", "21-10-2025") 

    assert birthday.calculate_age("Person1") == 24
    assert birthday.calculate_age("Person2") == 0
