__author__ = 'igor'

# Dictionary for format
timeFields = {'hours': 0,
              'minutes': 0,
              'seconds': 0};

def hourFormat(seconds, timeFields):
    timeFields['hours'] = seconds / 3600
    seconds -= timeFields['hours'] * 3600

    timeFields['minutes'] = seconds / 60
    seconds -= timeFields['minutes'] * 60

    timeFields['seconds'] = seconds

    return

#1. Read the value
seconds = input()

# 2. Calculate the smallest possible number of notes for the input value
hourFormat(seconds, timeFields)

# 3. Show the results
print("%d:%d:%d" % (timeFields['hours'], timeFields['minutes'], timeFields['seconds']))
