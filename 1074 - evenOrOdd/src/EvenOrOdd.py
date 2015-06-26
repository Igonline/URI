# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

valueN = input()
for i in range(0, valueN):
    num = input()
    if (num % 2 == 0) and (num < 0):
        print("EVEN NEGATIVE")
    elif (num % 2 == 0) and (num > 0):
        print("EVEN POSITIVE")
    elif (num % 2 != 0) and (num > 0):
        print("ODD POSITIVE")
    elif (num % 2 != 0) and (num < 0):
        print("ODD NEGATIVE")
    elif (num == 0):
        print("NULL")