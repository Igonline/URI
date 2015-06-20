__author__ = 'igor'

employeeSalary = float(input())

if (employeeSalary >= 0 and employeeSalary <= 400):
    percIncrease = 15.0
    moneyEarned = employeeSalary * percIncrease / 100
elif (employeeSalary > 400 and employeeSalary <= 800):
    percIncrease = 12.0
    moneyEarned = employeeSalary * percIncrease / 100
elif (employeeSalary > 800 and employeeSalary <= 1200):
    percIncrease = 10.0
    moneyEarned = employeeSalary * percIncrease / 100
elif (employeeSalary > 1200 and employeeSalary <= 2000):
    percIncrease = 7.0
    moneyEarned = employeeSalary * percIncrease / 100
elif (employeeSalary > 2000):
    percIncrease = 4.0
    moneyEarned = employeeSalary * percIncrease / 100

newSalary = employeeSalary + moneyEarned

print("Novo salario: %.2f" % newSalary)
print("Reajuste ganho: %.2f" % moneyEarned)
print("Em percentual: %.0f %%" % percIncrease)
