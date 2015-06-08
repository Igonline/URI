# coding=utf-8
__author__ = 'igor'

values = raw_input().split()
values = [int (i) + 1 for i in values]

# Se os valores de início e fim forem iguais, o jogo durou 24h
if (values[0] == values[1]):
    gameDuration = 24

# Se o jogo terminar no outro dia,
# somar as horas restantes do primeiro dia (24 - values[0]) às
# horas do outro dia (values[1])
elif (values[1] / values[0] == 0):
    gameDuration = (24 - values[0]) + values[1]

# Se o jogo iniciou e terminou no mesmo dia, apenas efetuar a diferença
else:
    gameDuration = values[1] - values[0]

print("O JOGO DUROU %d HORA(S)" % gameDuration)