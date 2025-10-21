# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Birthday:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # all_birthdays = {}
        # Parameters:
        # Side effects:
        #   Sets the name and birthday property 
        pass # No code here yet

    def add_record(self, name, birthday):
        # Parameters:
        #   name: string representing friend's name
        #   birthday: string representing friend's birthday
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds birthday record to self.birthdays
        pass # No code here yet

    def get_record(self, name):
        # Parameters:
        #   name: string representing friend's name
        # Returns:
        #   string: birthday corresponding to friend
        # Side-effects
        pass # No code here yet

    def get_all_records(self):
        # Returns:
        #   dictionary: self.birthdays

    def update_record(self, name, updated_birthday):
        # Parameters:
        #   name: string representing friend's name
        #   updated_birthday: string representing friend's birthday
        # Returns:
        #   None
        # Side-effects:
        #   Updates record in self.birthdays
        pass # No code here yet

    def edit_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string representing friend's old name
        #   new_name: string representing 
        # Returns:
        #   True or False if new name exists 
        # Side-effects
        #   update friend's name in the dictionary
        pass # No code here yet

    def birthday_reminder(self):
        # Parameters:
        # Returns:
        #   A list of friends' names whose birthdays are in less than 7 days
        #   else "No birthdays coming up"
        # Side-effects
        pass # No code here yet

    def calculate_age(self, names, today):
        # Parameters:
        #   name: list representing friend's name
        #   today: datetime object representing today's date
        # Returns:
        #   dictionary: name of friend and corresponding age
        # Side-effects
        pass # No code here yet


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given empty name and empty birthday
birthdays list is initialised 
"""
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
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
