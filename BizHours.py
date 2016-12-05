## BizHours - Class
# small class to handle instantiation of business objects,
# which are to be used with timeDrill1.py
# @args - int: GMT offset
#       - str: City Name
import time
class BizHours:
    def __init__(self, offset, name):
        self.name = name
        self.currentTime = (time.gmtime()[3] + offset)
        self.open = (self.currentTime >= 9 and self.currentTime < 21)

        
        
