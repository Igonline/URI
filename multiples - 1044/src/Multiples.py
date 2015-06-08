__author__ = 'igor'

numbers = raw_input().split()
A, B = [int(i) for i in numbers]

if (A > B) and (A % B == 0) or (B > A) and (B % A == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")



