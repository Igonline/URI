# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

values = []
count = 0
for i in range(0,5):
    num = input()
    values.append(num)
    if (num % 2 == 0):
        count = count + 1


print("%d valores pares" % count)

