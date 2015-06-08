__author__ = 'igor'

# Dictionary for format
timeFields = {'years': 0,
              'months': 0,
              'days': 0};

def timeFormat(days, timeFields):
    timeFields['years'] = days / 365
    days -= timeFields['years'] * 365

    timeFields['months'] = days / 30
    days -= timeFields['months'] * 30

    timeFields['days'] = days

    return

#1. Read the value
days = input()

# 2. Calculate how many years, months and days there are in the input value
timeFormat(days, timeFields)

# 3. Show the results
print("%d ano(s)\n"
      "%d mes(es)\n"
      "%d dia(s)"
      % (timeFields['years'], timeFields['months'], timeFields['days']))
