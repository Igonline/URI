# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

# TODO use functions (or refactor some other way)

valueX = input()
valueY = input()
sum = 0
if (valueX < valueY):
    for i in range(valueX+1, valueY):
        if (i % 2 != 0):
            sum = sum + i
else:
    for i in range(valueY+1, valueX):
        if (i % 2 != 0):
            sum = sum + i

print sum