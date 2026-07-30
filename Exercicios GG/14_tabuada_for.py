#Faça um programa que leia um número qualquer e mostre
#na tela a sua tabuada, utilizando um laço for

numero = int(input("Me dê um número e direi a tabuada: "))

for c in range(1, 11):
    resultado = (numero * c)
    print(f" {numero} x {c} = {resultado}")
print("FIM")

