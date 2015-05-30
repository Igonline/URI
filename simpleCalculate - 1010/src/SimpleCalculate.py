__author__ = 'igor'

product1 = raw_input().split(' ')
product2 = raw_input().split(' ')

totalAmount = float(product1[1]) * float(product1[2]) + float(product2[1]) * float(product2[2])

print "VALOR A PAGAR: R$ %.2f" %totalAmount
