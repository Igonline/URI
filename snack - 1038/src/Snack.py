__author__ = 'igor'

values = raw_input().split(' ')
values = [int(i) for i in values]
x, y = values

if x == 1:
    total = y * 4.00
elif x == 2:
    total = y * 4.50
elif x == 3:
    total = y * 5.00
elif x == 4:
    total = y * 2.00
elif x == 5:
    total = y * 1.50

print("Total: R$ %.2f" % total)