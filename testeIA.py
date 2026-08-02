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


# Exercício: Tabela de preços com tuplas
# Crie uma tupla contendo nomes de produtos e seus respectivos preços.
# Em seguida, exiba os produtos e preços organizados em uma tabela.

produtos = (
    ("Lápis", 2.50),
    ("Caderno", 15.90),
    ("Borracha", 1.75),
    ("Mochila", 89.90),
)

print("-" * 35)
print("TABELA DE PREÇOS")
print("-" * 35)

for nome, preco in produtos:
    print(f"{nome:.<25} R${preco:>7.2f}")

print("-" * 35)

# Explicação:
# 'produtos' é uma tupla que armazena outras tuplas.
# Cada tupla interna possui o nome de um produto e seu preço.
# O laço 'for' percorre cada produto, separando nome e preço.
# A formatação deixa a saída organizada como uma tabela.
