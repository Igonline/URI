__author__ = 'Igor Guimarães Dias <igonline15@gmail.com>'

# TODO use try catch code block to validade the presence of the key in the dict ddd_destination

ddd_destination = {61: 'Brasilia', \
                   71: 'Salvador', \
                   11: 'Sao Paulo', \
                   21: 'Rio de Janeiro', \
                   32: 'Juiz de Fora', \
                   19: 'Campinas', \
                   27: 'Vitoria', \
                   31: 'Belo Horizonte'}

ddd = input()

if ddd in ddd_destination:
    print ddd_destination[ddd]
else:
    print("DDD nao cadastrado")