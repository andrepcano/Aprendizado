# Exercício 13

numero = int(input("Digite um número inteiro e direi se é par ou ímpar: "))
par = numero %2 == 0
impar = numero %2 != 0

if par:
    print(f"O número {numero} é PAR!!")
else:
    print(f"O número {numero} é IMPAR!!")

