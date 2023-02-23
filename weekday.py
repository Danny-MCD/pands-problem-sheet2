# programme to let you know when run if it is currently a weekday or the weekend
# Author:  Daniel Mc Donagh

# import the datetime module
from datetime import datetime

# sets dc object to current date using now()
dc = datetime.now()

# set x to weekday function in datetime module
x = dc.weekday()

# weekday() sets day of week to integer value starting Monday=0
# if else commands used to seperate weekdays from weekend
if (x<5):
    print("Today is a weekday")
else:
    print("Hurray, It is the weekend")
