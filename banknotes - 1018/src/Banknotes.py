__author__ = 'igor'

# Dictionary for notes
notes = {'hundred': 0,
         'fifty': 0,
         'twenty': 0,
         'ten': 0,
         'five': 0,
         'two': 0,
         'one': 0};

def calcSmallestNumberOfNotes(value, notes):
#while(value != 0):
    notes['hundred'] = value / 100
    value -= notes['hundred'] * 100

    notes['fifty'] = value / 50
    value -= notes['fifty'] * 50

    notes['twenty'] = value / 20
    value -= notes['twenty'] * 20

    notes['ten'] = value / 10
    value -= notes['ten'] * 10

    notes['five'] = value / 5
    value -= notes['five'] * 5

    notes['two'] = value / 2
    value -= notes['two'] * 2

    notes['one'] = value / 1
    value -= notes['one'] * 1

    return notes

#1. Read the value
value = input()

# 2. Calculate the smallest possible number of notes for the input value
calcSmallestNumberOfNotes(value, notes)

# 3. Show the results
print("%d\n" \
      "%d nota(s) de R$ 100,00\n"
      "%d nota(s) de R$ 50,00\n"
      "%d nota(s) de R$ 20,00\n"
      "%d nota(s) de R$ 10,00\n"
      "%d nota(s) de R$ 5,00\n"
      "%d nota(s) de R$ 2,00\n"
      "%d nota(s) de R$ 1,00"
      % (value,
         notes['hundred'],
         notes['fifty'],
         notes['twenty'],
         notes['ten'],
         notes['five'],
         notes['two'],
         notes['one']
        )
      )
