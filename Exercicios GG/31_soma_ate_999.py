#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando digitar 999. 
#No final mostre quantos numeros foram digitados e o resultado da soma.

numero = int(input("Digite um valor (999 para parar): "))
soma = 0
quantidade = 0

while (numero != 999):
    numero = int(input("Digite um valor (999 para parar): "))
    soma += numero
    quantidade += 1

print("a soma dos {} valores é: {}".format(quantidade, soma))

