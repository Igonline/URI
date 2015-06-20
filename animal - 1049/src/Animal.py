__author__ = 'igor'

# TODO use binary trees to store taxonomical classification

word1 = raw_input()
word2 = raw_input()
word3 = raw_input()

if (word1 == "vertebrado"):
    if (word2 == "ave"):
        if(word3 == "carnivoro"):
            animal = "aguia"
        else:
            animal = "pomba"
    else:
        if (word3 == "onivoro"):
            animal = "homem"
        else:
            animal = "vaca"
else:
    if (word2 == "inseto"):
        if (word3 == "hematofago"):
            animal = "pulga"
        else:
            animal = "lagarta"
    else:
        if (word3 == "hematofago"):
            animal = "sanguessuga"
        else:
            animal = "minhoca"

print animal