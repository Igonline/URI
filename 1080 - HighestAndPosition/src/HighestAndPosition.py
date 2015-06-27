# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

intList = []
for i in range(0, 100):
    number = input()
    intList.append(number)

maxValue = max(intList)
indexOfMaxValue = intList.index(maxValue)
print maxValue
print (indexOfMaxValue + 1)

