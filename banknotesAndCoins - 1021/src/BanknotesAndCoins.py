__author__ = 'igor'

# Dictionary for notes
notes = {'hundred': 0,
         'fifty': 0,
         'twenty': 0,
         'ten': 0,
         'five': 0,
         'two': 0,
         'one': 0};

# Dictionary for coins
coins = {'dollar': 0,
         'half': 0,
         'quarter': 0,
         'dime': 0,
         'nickel': 0,
         'penny': 0};

def calcSmallestNumberOfNotes(value, notes):
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

def calcSmallestNumberOfCoins(value, coins):
    coins['dollar'] = int(value / 1.00)
    value -= coins['dollar'] * 1.00

    coins['half'] = int(value / 0.50)
    value -= coins['half'] * 0.50

    coins['quarter'] = int(value / 0.25)
    value -= coins['quarter'] * 0.25

    coins['dime'] = int(value / 10)
    value -= coins['dime'] * 10


# Por algum motivos dos diabos, executar int(value/0.05), com value valendo 0.05, dá 0!!!!
# REBOLAR para consertar isso e fazer int(value/0.05) dar 1
    coins['nickel'] = int(value / 0.05)
    print("value: %f" % value)
    print("int 1.0000: %d" % int(0.050000 / 0.05))
    print("valeu / 0.05: %d" % int(value / 0.05))

    print("coins['nickel'] = %f" % coins['nickel'])
    value -= coins['nickel'] * 0.05


    coins['penny'] = int(value / 0.01)
    value -= coins['penny'] * 0.01

    return coins

#1. Read the value
fValue = float( raw_input() )
iValue = int(fValue)

# 2. Calculate the smallest possible number of notes for the input value
calcSmallestNumberOfNotes(iValue, notes)

# 3. Calculate the decimal part of the value
decimalPartOfValue = fValue - iValue

# 4. Calculate smallest possible number of coins for the input value
calcSmallestNumberOfCoins(decimalPartOfValue, coins)

# 5. Show the results for integer part of value
print("%d\n"
      "%d nota(s) de R$ 100,00\n"
      "%d nota(s) de R$ 50,00\n"
      "%d nota(s) de R$ 20,00\n"
      "%d nota(s) de R$ 10,00\n"
      "%d nota(s) de R$ 5,00\n"
      "%d nota(s) de R$ 2,00\n"
      "%d nota(s) de R$ 1,00"
      % (fValue,
         notes['hundred'],
         notes['fifty'],
         notes['twenty'],
         notes['ten'],
         notes['five'],
         notes['two'],
         notes['one']
        )
      )

# 6. Show the results for decimal part of value
print("%.2f\n"
      "%d moeda(s) de R$ 1,00\n"
      "%d moeda(s) de R$ 0,50\n"
      "%d moeda(s) de R$ 0,25\n"
      "%d moeda(s) de R$ 0,10\n"
      "%d moeda(s) de R$ 0,05\n"
      "%d moeda(s) de R$ 0,01\n"
      % (decimalPartOfValue,
         coins['dollar'],
         coins['half'],
         coins['quarter'],
         coins['dime'],
         coins['nickel'],
         coins['penny']
        )
      )
