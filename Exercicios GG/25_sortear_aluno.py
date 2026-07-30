#Um professor quer sortear um de seus quatro alunos para apagar
#o quadro. Faça um programa que ajude ele, lendo o nome deles e 
#escrevendo o nome do escolhido

from random import choice

nome_1 = input("Nome do 1 aluno: ")
nome_2 = input("Nome do 2 aluno: ")
nome_3 = input("Nome do 3 aluno: ")
nome_4 = input("Nome do 4 aluno: ")
lista = [nome_1, nome_2, nome_3, nome_4]

escolhido = choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))

