# -*- coding=utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

values = []
posit = sum = media = 0
for i in range(0,6):
    num = float(input())
    values.append(num)
    if (num > 0):
        posit = posit + 1
        sum =  sum + num

media = sum / posit
print("%d valores positivos" % posit)
print("%.1f" % media)
