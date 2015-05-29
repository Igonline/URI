__author__ = 'igor'

aWeight = 2.0
bWeight = 3.0
cWeight = 5.0

a = input()
b = input()
c = input()

weighted_sum = (aWeight * a) + (bWeight * b) + (cWeight * c)
media = weighted_sum / (aWeight + bWeight + cWeight)
print "MEDIA = %.1f" % media
