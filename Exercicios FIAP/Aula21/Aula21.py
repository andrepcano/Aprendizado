#1) Escreva uma função que receba uma lista de strings como argumento e retorne um dicionário onde as chaves 
#sejam as palavras e os valores sejam o número de vezes que essas palavras aparecem na lista. 
#Exemplo de entrada:{"casa": 2, "carro": 3, "bicicleta": 2}

'''list_palavras = ["Carro", "Casa", "Bicicleta", "Autonomo", "Casa", "Bicicleta"]
contagem = {}

def retorno_dict(list):
    for palavra in list_palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    print(contagem)

retorno_dict(list_palavras)'''




#2) Dada a tupla pessoas = (("João", 19), ("Maria", 21), ("Pedro", 20), ("Ana", 18)), escreva uma 
#função que receba uma tupla semelhante a pessoas e retorne uma nova tupla contendo apenas as 
#pessoas que são maiores de idade (idade ≥ 18).

'''pessoas = (("João", 19), 
           ("Maria", 21), 
           ("Pedro", 20), 
           ("Ana", 18))

def maiores_de_idade(pessoas):
    resultado = []

    for pessoa in pessoas:
        nome = pessoa[0]
        idade = pessoa[1]

        if idade >= 21:
            resultado.append(pessoa)
    return tuple(resultado)

print(maiores_de_idade(pessoas))'''




#3) Implemente uma função que receba uma lista de números inteiros e ordene essa lista utilizando o algoritmo de Bubble Sort.

'''lista = [5, 2, 8, 1]

for i in range(len(lista)):
    for j in range(len(lista) -1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)'''




#4) Escreva uma função que receba uma lista de tuplas, onde cada tupla contém dois números inteiros. A função deve 
#retornar uma lista contendo a soma de cada par de números nas tuplas.Exemplo de entrada: pares = [(1, 2), (3, 4), (5, 6)]  


#5) Escreva uma função que receba uma lista de nomes de alunos e uma lista correspondente de notas. A função deve retornar um dicionário 
#onde as chaves são os nomes dos alunos e os valores são suas respectivas notas: alunos = ["Ana", "Bruno", "Carlos", "Diana"], 
#notas = [85, 90, 78, 92]Exemplo de saída: {"Ana": 85, "Bruno": 90, "Carlos": 78, "Diana": 92}


#6) Imagine que você tem um dicionário que armazena o saldo de várias contas bancárias. Escreva uma função que receba o dicionário de contas e um segundo dicionário
#contendo valores a serem creditados ou debitados das respectivas contas. A função deve atualizar o saldo das contas existentes e criar novas entradas 
#para contas que ainda não existem

'''saldos = {"Conta A": 1000, "Conta B": 1500}
movimentacoes = {"Conta A": -200, "Conta C": 500}

def att_saldos(saldos, movimentacoes):
    for conta in movimentacoes:
        if conta in saldos:
            saldos[conta] += movimentacoes[conta]
        else:
            saldos[conta] = movimentacoes[conta]
        return saldos

print(att_saldos(saldos, movimentacoes))'''




#7) Escreva uma função que receba uma lista de palavras e ordene-a em ordem alfabética utilizando o algoritmo Bubble Sort.

'''palavras = ["banana", "maçã", "laranja", "uva", "abacaxi"] 

def ordenar(palavras):
    for palavra in range(len(palavras)):
        for letra in range(len(palavras) - 1):
            if palavras[letra] > palavras[letra + 1]:
                palavras[letra], palavras[letra + 1] = palavras[letra + 1], palavras[letra] 
    return palavras

print(ordenar(palavras))'''




#8) Escreva uma função que receba um dicionário com o nome de produtos e seus respectivos preços, e um valor limite. A função deve retornar um novo dicionário
#contendo apenas os produtos cujo preço seja maior que o limite fornecido. Exemplo de Entrada: produtos = {"banana": 2.50, "maçã": 3.20, "laranja": 1.80}
#limite = 2.00

produtos = {"banana": 2.50, "maçã": 3.20, "laranja": 1.80}
limite = 2.00
produtos_maior_limite = {}

def maior_limite(produtos, limite):
    for produto in produtos:
        if produtos[produto] > limite:
            produtos_maior_limite[produto] = produtos[produto]
    return produtos_maior_limite

print(maior_limite(produtos, limite))






