__author__ = 'igor'

employeeNumber = input()
hoursWorkedPerMonth = input()
paymentPerHour = input()

monthSalary = hoursWorkedPerMonth * paymentPerHour

print "NUMBER = %.0f" % employeeNumber
print "SALARY = U$ %.2f" % monthSalary