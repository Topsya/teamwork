from collections import UserDict
from datetime import datetime, timedelta
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass
    
class Phone(Field):
    def __init__(self,phone):
        self.phone = phone