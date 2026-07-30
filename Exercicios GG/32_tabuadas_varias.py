#Faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor digitado pelo user
#O programa sera interrompido quando o numero digitado for negativo

while True:
    try:
        numero = float(input("Digite um numero para calcular a tabuada (negativo para sair): "))
    except ValueError:
        print("Número Inválido!")
        continue

    if numero < 0:
        print("Programa Terminado!")
        break

    for i in range(1, 11):
        print(f"{numero:g} x {i} = {numero * i:g}")

