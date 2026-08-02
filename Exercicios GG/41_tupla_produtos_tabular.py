#Crie um programa que tenha uma tupla unica com nome dos produtos e seus respectivos preços na sequencia
#no final, mostre uma listagem dos preços, organizando os dados de forma tabular

produtos = (
    ("Livro", 45.99),
    ("Celular", 1000.00),
    ("Mochila", 150.00),
    ("Fone do Ouvido", 500.00),
)

print("-" * 35)
print("Lista de Produtos: ")
print("-" * 35)

for nome, preco in produtos:
        print(f"{nome:.<25} R${preco:>7.2f}")

print("-" * 35)

