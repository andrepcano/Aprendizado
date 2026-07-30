# Exercício 20

estoques = [{'livro': '1984', 'quantidade': 1},
    {'livro': 'Dom Casmurro', 'quantidade': 32}]

for estoque in estoques:
    if estoque['quantidade'] > 0:
        print(f"Livro disponível: {estoque['livro']}")

compra = input(f"Você deseja comprar qual livro: ")

for estoque in estoques:
    if estoque ['livro'] == compra and estoque['quantidade'] > 0:
        estoque["quantidade"] -= 1
        print(f"Parabéns pela compra do livro: {estoque['livro']} ")
        print(f"Quantidade atual: {estoque['quantidade']}")
        break;
    else:
        print("Desculpe, Livro Esgotado!!")

