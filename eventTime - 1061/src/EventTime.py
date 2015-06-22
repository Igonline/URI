# -*- coding=utf-8 -*-

__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

from datetime import timedelta

def calcTimeSpent(initDay, initTime, endDay, endTime):
    timeSpent = []

    time1 = timedelta(days=initDay, hours=initTime[0], minutes=initTime[1], seconds=initTime[2])
    time2 = timedelta(days=endDay, hours=endTime[0], minutes=endTime[1], seconds=endTime[2])
    delta = time2 - time1
    timeSpent.insert(0, delta.days) # get days with days attribute
    timeSpent.insert(1, delta.seconds / 3600) # get hours with integer division
    timeSpent.insert(2, (delta.seconds % 3600) / 60) # get minutes with seconds remainder and integer division
    timeSpent.insert(3, ((delta.seconds % 3600) % 60) % 60) # similarly, get seconds with remainder
    return timeSpent

initDay = raw_input().split()
initTime = raw_input().split(" : ")
endDay = raw_input().split()
endTime = raw_input().split(" : ")

# Prepara os dados
initDay = int(initDay[1])
initTime = [int (i) + 1 for i in initTime]
endDay = int(endDay[1])
endTime = [int (i) + 1 for i in endTime]

# Calculo o tempo gasto
timeSpent = calcTimeSpent(initDay, initTime, endDay, endTime)

# Exibe o resultado
print("%d dia(s)" % timeSpent[0])
print("%d hora(s)" % timeSpent[1])
print("%d minuto(s)" % timeSpent[2])
print("%d segundo(s)" % timeSpent[3])

