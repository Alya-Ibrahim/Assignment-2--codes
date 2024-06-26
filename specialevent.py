# -*- coding: utf-8 -*-
"""SpecialEvent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PKzTiRDK4nP17DCu572c8xxOTStZC4Tk
"""

# Import the Event class to inherit from it.
from Event import Event

# SpecialEvent class that inherits from Event
class SpecialEvent(Event):
    # Constructor of SpecialEvent with parameters for all its attributes and those of Event.
    def __init__(self, name, location, duration, date, purpose):
        # Call the constructor of the parent class (Event)
        super().__init__(name, location, duration, date)
        self.purpose = purpose  # Set the purpose of the SpecialEvent

    # Getter method for purpose
    def get_purpose(self):
        return self.purpose

    # Setter method for purpose
    def set_purpose(self, purpose):
        self.purpose = purpose