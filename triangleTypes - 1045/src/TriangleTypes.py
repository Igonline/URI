__author__ = 'igor'

values = raw_input().split()
values = [float(i) for i in values]
values.sort()
values.reverse()
A, B, C = values

if (A >= B + C):
    print("NAO FORMA TRIANGULO")
elif (A == (B**2 + C**2)**0.5):
    print("TRIANGULO RETANGULO")
elif ((A > (B**2 + C**2)**0.5)):
    print("TRIANGULO OBTUSANGULO")
elif ((A < (B**2 + C**2)**0.5)):
    print("TRIANGULO ACUTANGULO")
if (A == B) and (B == C):
    print("TRIANGULO EQUILATERO")
elif (A == B) and (A != C) or (A == C) and (A != B) or (B == C) and (B != A):
    print("TRIANGULO ISOSCELES")







