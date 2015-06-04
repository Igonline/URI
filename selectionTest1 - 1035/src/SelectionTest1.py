__author__ = 'igor'

values = raw_input().split(' ')

values = [int(i) for i in  values]

A, B, C, D = values

if (B > C) and (D > A) and (C + D) > (A + B) and (C > 0) and (D > 0) and (A % 2 == 0) :
    #and (A % 2 == 0)
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

