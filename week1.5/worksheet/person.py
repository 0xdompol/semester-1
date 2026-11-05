# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        self.name = name
        self.birth = birth
        if type(self.name) != str:
            raise TypeError("name must be a string")
        elif len(self.name) == 0:
            raise ValueError("name must not be empty")
        if type(self.birth) != date:
            raise TypeError("birth must be a date object")
    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        Returns the initials of the person in uppercase
        """
        initials = self.name[0].upper()
        x = 0
        while 1:
            try:
                index = self.name.index(" ",x)
                initials += self.name[index + 1].upper()
                x = index + 1
            except ValueError:
                break
        return initials

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False if not.
        """
        today = date.today()
        return True if (self.birth == today) else False
    # (see README.md for further details)