#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuario o valor a ser sacado(numero inteiro)
#e o programa vai informar quantas cedulas de cada valor serao entregues OBS: O caixa tem notas de R$50, R$20, R$10, R$1

while True:
    try:
        saque = int(input("Digite o valor do saque: "))
    except ValueError:
        print("Digite o valor correto!")
        continue

    if saque > 0:
        print("Saque válido")
        print("Calculando notas...")
        notas_50 = saque // 50
        resto = saque % 50
        notas_20 = resto // 20
        resto = resto % 20
        notas_10 = resto // 10
        resto = resto % 10
        notas_1 = resto // 1
        print(f"O saque de {saque} precisou de: \n{notas_50} notas de 50, \n{notas_20} notas de 20, \n{notas_10} notas de 10, \n{notas_1} noats de 1")
        break
    else:
        print("Digite um valor maior que zero!")
    
    

    
