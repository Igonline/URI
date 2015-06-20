# coding=utf-8
__author__ = 'igor'

values = raw_input().split()
values = [int (i) + 1 for i in values]

## CALCULO DAS HORAS

# Se os valores de início e fim forem iguais, o jogo durou 24h
if (values[0] == values[2]):
    gameHours = 24

# Se o jogo terminar no outro dia,
# somar as horas restantes do primeiro dia (24 - values[0]) às
# horas do outro dia (values[1])
elif (values[2] / values[0] == 0):
    gameHours = (24 - values[0]) + values[2]

# Se o jogo iniciou e terminou no mesmo dia, apenas efetuar a diferença
else:
    gameHours = values[2] - values[0]

## CALCULO DOS MINUTOS

# Transforma as horas em minutos, subtrai dos minutos passados do horário de inicío e
# soma com os minutos adicionais proveniente do horário de término
gameMinutes = gameHours * 60 - values[1] + values[3]

## CALCULO DA DURAÇÃO DO JOGO

# Espera-se um divisão inteira aqui
gameDuration = [0, 0]
gameDuration[0] = gameMinutes / 60
gameDuration[1] = gameMinutes % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (gameDuration[0], gameDuration[1]))