# Exercício 34

numero = float(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar")
elif numero == 0:
    print("O número é 0!")
else:
    print("O número é NEGATIVO!")

