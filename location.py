# -*- coding: utf-8 -*-
"""Location.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fC0hAGkW_XSaJanQZzfUHGRsIswWk1x
"""

# Import the MuseumLocationType enum to use for type hinting.
from MuseumLocationType import MuseumLocationType

# Location class definition
class Location:
    # Constructor of Location with parameters for all its attributes.
    def __init__(self, name, type: MuseumLocationType):
        self.name = name  # Set the name of the Location
        self.type = type  # Set the type of the Location, expected to be a MuseumLocationType

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for type
    def get_type(self):
        return self.type

    # Setter method for type
    def set_type(self, type):
        if isinstance(type, MuseumLocationType):
            self.type = type
        else:
            raise ValueError("Invalid MuseumLocationType")  # Raise an error if the type is not a MuseumLocationType