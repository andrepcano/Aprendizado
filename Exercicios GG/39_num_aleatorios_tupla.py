#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que esta na tupla

from random import randint

num_aleatorios = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior_numero = num_aleatorios[0] 
menor_numero = num_aleatorios[0]

for numero in num_aleatorios:
    print(f"Numero gerado: {numero}")
    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero: 
        menor_numero = numero

print(f"\nMaior Número: {maior_numero}")
print(f"\nMenor Número: {menor_numero}")











