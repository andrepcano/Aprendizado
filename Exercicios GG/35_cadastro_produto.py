#Crie um programa que leia o nome e o preço de varios produtos. O programa deve perguntar se o user quer continuar,
#No final mostre: A) Qual total gasto na compra, B) Quantos produtos custam mais de R$1000, C) Qual o nome do produto mais barato

prod_mais_de_1000 = 0
prod_mais_barato = 10000000000000000000000000000000000000000000
nome_prod_mais_barato = ""
total = 0

while True:
    nome_prod = input("Nome do produto: ")

    while True:
        try:
            preco_prod = float(input("Digite o preço: "))
            break
        except ValueError:
            print("Digite o valor correto!")

    if preco_prod > 1000:
        prod_mais_de_1000 += 1

    if preco_prod < prod_mais_barato:
        prod_mais_barato = preco_prod
        nome_prod_mais_barato = nome_prod
    
    total += preco_prod
    
    decisao = input("Quer continuar? (s) ou (n): ").lower()
    while decisao not in ("s", "n"):
        print("Digite corretamente!")
        decisao = input("Quer continuar cadastrando? (s) ou (n): ").lower()
    
    if decisao == "n":
        print(f"Total gasto {total}")
        print(f"Quantidade de produtos que custam mais de R$1000: {prod_mais_de_1000}")
        print(f"Nome do produto mais barato {nome_prod_mais_barato}")
        break

    


