# -*- coding=utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

salary = float(input())

if (salary > 0 and salary <= 2000):
    taxRate = 0
elif (salary > 2000 and salary <= 3000):
    taxRate = 8
    totalTaxes = 8 * (salary - 2000) / 100.0
elif (salary > 3000 and salary <= 4500):
    taxRate = 18
    totalTaxes = 8 * 1000 / 100.0 + \
                 18 * (salary - 3000) / 100.0
elif (salary > 4500):
    taxRate = 8
    totalTaxes = 8 * 1000 / 100.0 + \
                 18 * 1500 / 100.0 + \
                 28 * (salary - 4500) / 100.0

if (taxRate == 0):
    print("Isento")
else:
    print("R$ %.2f" % totalTaxes)