# -*- coding: utf-8 -*-
"""Event.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v6dg8Aqf98j6BJg74OFH8E5AdHWpnftf
"""

# Import the Location class to use for type hinting.
from Location import Location

#Here it is defining the class event
class Event:
    #A constructor of Event with parameters for all its attributes.
    def __init__(self, name, location: Location, duration, date):
        self.name = name  # Set the name of the Event
        self.location = location  # Set the location of the Event, expected to be a Location object
        self.duration = duration  # Set the duration of the Event (in minutes)
        self.date = date  # Set the date of the Event

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for location
    def get_location(self):
        return self.location

    # Setter method for location
    def set_location(self, location):
        if isinstance(location, Location):
            self.location = location
        else:
            raise ValueError("Invalid location type")  # Raise an error if the location is not a Location object

    # Getter method for duration
    def get_duration(self):
        return self.duration

    # Setter method for duration
    def set_duration(self, duration):
        self.duration = duration

    # Getter method for date
    def get_date(self):
        return self.date

    # Setter method for date
    def set_date(self, date):
        self.date = date