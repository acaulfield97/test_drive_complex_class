from lib.birthday import *
import pytest

"""
birthdays list is initialised 
"""
def test_initialise_empty_birthday_list():
    birthday = Birthday(self)
    assert birthday.birthdays == {}

"""
Given a name and a birthday
#add_record adds friends name and birthday to birthdays dictionary
"""
birthday = Birthday(self)
birthday.add_record("person1", "01-01-2000")
assert birthday.get_record("Person1") == "01-01-2000"

"""
Given a name and updated birthday
#update_record updates birthdays dictionary with friend's name and new birthday
"""
birthday = Birthday(self)
birthday.add_record("Person1", "01-01-2000")
birthday.update_birthday("Person1", "01-02-2000")
assert birthday.get_record("Person1") == "01-02-2000"

"""
Given old name and new name
#edit_name changes friend's name to new_name and updates dictionary
"""
birthday = Birthday(self)
birthday.add_record("Person1", "01-01-2000")
birthday.edit_name("Person1", "New Person")
assert "Person1" not in self.birthdays
assert "New Person" in self.birthdays

"""
#birthday_reminder returns list of friends birthdays that are in 7 days or less
"""
birthday = Birthday()
birthday.add_record("Person1", "01-01-2000")
birthday.add_record("Person2", "02-02-1990")
assert birthday.birthday_reminder() == ["Person1", "Person2"]

"""
Given a list of friends names and today's date
Returns a new dictionary of friends names and their ages
"""
birthday = Birthday()
birthday.add_record("Person1", "11-11-2000") 
birthday.add_record("Person2", "21-10-2025") 

assert birthday.calculate_ages("Person1", datetime.today()) == 24
assert birthday.calculate_ages("Person1", datetime.today()) == 0