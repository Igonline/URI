# -*- coding: utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

numOfTestCases = input()
testCases = []
for i in range(0, numOfTestCases):
    tc = raw_input().split()
    tc = [float(i) for i in tc]
    testCases.append(tc)


for i in range(0, numOfTestCases):
    weightedSum = 0
    media = 0

    weightedSum = 2 * testCases[i][0] + 3 * testCases[i][1] + 5 * testCases[i][2]
    sumOfWeights = 10.0
    media = weightedSum / sumOfWeights
    print("%.1f" % media)