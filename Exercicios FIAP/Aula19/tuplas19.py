# TUPLAS 

# a = (1, 10, True, "Ok")
# print(a[0:3])

# TRANSFORMANDO
# a = [1, 2, 3, 4, 5]
# b = tuple(a)
# c = list(b)
# print(c)

# CONCATENAR TUPLAS
# igual concatenar listas
#a = (1, 2, 3, 4)
#b = (5, 6, 7, 8)
#c = a + b


#
# a = [10, 4.5, 6, 9, 0]

# for i in range(len(a)):
#     print(i, a[i])


#
#Crie uma maneira para adicionar elementos em uma tuplas. Sua função recebe a tuplas e o elemento
#a ser adicionado e retorna a tuplas final

'''tupla = (1, 2, 3, 5, 6)

def add_tupla(var):
    return tupla + (var,) # PRECISA DE UMA "," PARA ENTENDER COMO TUPLA

print(add_tupla("Andre"))'''


#Crie uma maneira para remover elementos em uma tupla. Sua função recebe a tupla e o index do elemento a ser removido
# e retorna a tupla final

'''tupla = (1, 2, 3, 4, 5, 6)

def remove_tupla(tupla, indice):               # tupla[indice + 1:] → pega o que vem depois
    return tupla[:indice] + tupla[indice + 1:] # tupla[:indice] → pega o que vem antes'''


# Escreva uma função que receba uma frase como parâmetro e retorne um dicionario, onde cada chave seja
# um caractere e seu valor seja o número de vezes que o caractere  aparece na frase lida.

'''def contar_caracteres(frase):
    dicionario = {}

    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1

    return dicionario

print(contar_caracteres("Os ratos"))'''



# CONJUNTOS

#Escreva um programa que compare duas listas. Utilizando operações de conjuntos, imprima:
#A) Os valores comuns das duas listas:

'''lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

cnjt1 = set(lista1)
cnjt2 = set(lista2)
print(cnjt1 & cnjt2) #INTERSEÇÃO'''

#B) Os valores que só existem na primeira

'''lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

cnjt1 = set(lista1)
cnjt2 = set(lista2)
print(cnjt1 - cnjt2) #PEGA APENAS OS QUE TEM EM AMBAS'''

#C) Os valores que existem apenas na segunda

'''lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

cnjt1 = set(lista1)
cnjt2 = set(lista2)
print(cnjt2 - cnjt1)'''

#D) Uma lista com os elementos não repetidos das duas listas (^)

'''lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

cnjt1 = set(lista1)
cnjt2 = set(lista2)
print(cnjt2 ^ cnjt1) #APENAS OS NÃO REPETIDOS'''


