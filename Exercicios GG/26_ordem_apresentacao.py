#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia o 
#nome dos quatro alunos e msotre a ordem sorteada

from random import shuffle

nome_1 = input("Nome do 1 aluno: ")
nome_2 = input("Nome do 2 aluno: ")
nome_3 = input("Nome do 3 aluno: ")
nome_4 = input("Nome do 4 aluno: ")
lista = [nome_1, nome_2, nome_3, nome_4]

ordem = shuffle(lista)
print("A ordem da apresentação será:")
print(lista)

