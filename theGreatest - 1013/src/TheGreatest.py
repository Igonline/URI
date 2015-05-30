# coding=utf-8
__author__ = 'igor'

def maiorAB (a, b):
    res = ( (a + b + abs(a-b)) ) / 2
    return res

# Recebe n parametros separados por um " " e já cria uma lista
values = raw_input().split(' ')

# List comprehension que faz cast para int (a lista estava em string por conta de raw_input
values = [int(x) for x in values]

a = values[0]
b = values[1]
c = values[2]

print ("%d eh o maior" % maiorAB(a, maiorAB(b, c)))