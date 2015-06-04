__author__ = 'igor'

values = raw_input().split(' ')

values = [float(i) for i in values]

a, b, c = values
delta = b**2 - 4 * a * c

if(a == 0) or (delta < 0):
    print("Impossivel calcular")
else:
    R1 = (b * -1 + pow(delta, 0.5)) / (2 * a)
    R2 = (b * -1 - pow(delta, 0.5)) / (2 * a)
    print ("R1 = %.5f" % R1)
    print ("R2 = %.5f" % R2)