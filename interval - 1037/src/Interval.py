__author__ = 'igor'

value = float(input())

if (value >= 0) and (value <= 25):
    print("Intervalo [0,25]")
elif (value > 25) and (value <= 50):
    print("Intervalo (25,50]")
elif (value > 50) and (value <= 75):
    print("Intervalo (50,75]")
elif (value > 75) and (value <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")