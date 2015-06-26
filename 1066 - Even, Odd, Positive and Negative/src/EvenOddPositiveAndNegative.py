# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

values = []
countPositive = countNegative = countEven = countOdd = 0
for i in range(0,5):
    num = input()
    values.append(num)
    if (num > 0):
        countPositive = countPositive + 1
    elif (num < 0):
        countNegative = countNegative + 1
    if (num % 2 == 0):
        countEven = countEven + 1
    else:
        countOdd = countOdd + 1

print("%d valor(es) par(es)" % countEven)
print("%d valor(es) impar(es)" % countOdd)
print("%d valor(es) positivo(s)" % countPositive)
print("%d valor(es) negativo(s)" % countNegative)

