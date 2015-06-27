# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

valueX = input()
valueY = input()
sum = 0
for i in range(valueX+1, valueY):
    if (i % 2 != 0):
        sum = sum + i