__author__ = 'igor'

values = raw_input().split(' ')
values = [float(i) for i in values]
x, y = values

if (x > 0.0) and (y > 0.0):
    print("Q1")
elif (x < 0.0) and (y > 0.0):
    print("Q2")
elif (x < 0.0) and (y < 0.0):
    print("Q3")
elif (x > 0.0) and (y < 0.0):
    print("Q4")
elif (x == 0.0) and (y != 0.0):
    print("Eixo Y")
elif (x != 0.0) and (y== 0.0):
    print("Eixo X")
else:
    print("Origem")