__author__ = 'igor'

values = raw_input().split(' ')
values = [float(i) for i in values]
n1, n2, n3, n4 = values

n1_Weight = 2.0
n2_Weight = 3.0
n3_Weight = 4.0
n4_Weight = 1.0

weightedSum = (n1_Weight * n1) + (n2_Weight * n2) + (n3_Weight * n3) + (n4_Weight * n4)
media = weightedSum / (n1_Weight + n2_Weight + n3_Weight + n4_Weight)


if (media < 5.0):
    print "Media: %.1f" % media
    print("Aluno reprovado.")
elif (media >= 5.0) and (media < 7.0):
    n_extra = float(input())
    print "Media: %.1f" % media
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % n_extra)
    new_media = (media + n_extra) / 2.0
    if (new_media <= 5.0):
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print("Media final: %.1f" % new_media)
else:
    print "Media: %.1f" % media
    print("Aluno aprovado.")