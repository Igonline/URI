# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

valueX = input()
for i in range(0,6):
    if (valueX % 2 != 0):
        print valueX + 2*i
    else:
        print valueX + 2*i + 1