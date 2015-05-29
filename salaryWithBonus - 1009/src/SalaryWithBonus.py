__author__ = 'igor'

salaryBonus = 0.15

employeeName = raw_input()
fixedSalary = input()
valueSold = input()

totalSalary = fixedSalary + salaryBonus * valueSold

print "TOTAL = R$ %.2f" % totalSalary