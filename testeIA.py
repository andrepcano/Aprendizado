""" Primeiro programa usando IA (codex)

while True:
    try:
        numero = float(input("Digite um número (negativo para sair): ").replace(",", "."))
    except ValueError:
        print("Digite um número válido.")
        continue

    if numero < 0:
        break

    for i in range(1, 11):
        print(f"{numero:g} x {i} = {numero * i:g}")"""


# Exercício 36: Simulador de caixa eletrônico
# O caixa possui notas de R$20, R$10, R$5 e R$1.
# O programa permite vários saques e termina ao informar um valor negativo.

while True:
    try:
        saque = int(input("\nDigite o valor do saque (negativo para sair): R$"))
    except ValueError:
        print("Digite apenas um número inteiro.")
        continue

    if saque < 0:
        print("Caixa eletrônico encerrado.")
        break

    if saque == 0:
        print("Digite um valor maior que zero.")
        continue

    restante = saque
    print(f"\nPara sacar R${saque}, você receberá:")

    # Para cada nota, calculamos quantas cabem no valor restante.
    for cedula in (20, 10, 5, 1):
        quantidade = restante // cedula
        restante = restante % cedula

        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${cedula}")
