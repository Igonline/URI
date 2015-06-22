# -*- coding=utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

counter = 0
for i in range(1,7):
    number = float(raw_input())
    if (number > 0):
        counter = counter + 1

print("%d valores positivos" % counter)