#LIST COMPREHENSION

# lista = [i for i in range(1, 6)]
# print(lista)

# lista = [i * 2 for i in range(1, 6)]
# print(lista)

# numeros = [1, 2, 3, 4, 5, 6]
# lista = [numero * 2 for numero in numeros]
# print(lista)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_pares = [numero for numero in numeros if numero % 2 == 0]
# print(lista_pares)


# numeros = [5, 12, 8, 20, 3, 15, 7, 30]
# lista_maiores_10 = [numero for numero in numeros if numero >= 10]
# print(lista_maiores_10)


# numeros = [1, 2, 3, 4, 5, 6]
# lista_dobra_pares = [numero * 2 for numero in numeros if numero % 2 == 0]
# print(lista_dobra_pares)


# numeros = [2, 4, 6, 8, 10]
# lista_quadrado_maiores_5 = [numero ** 2 for numero in numeros if numero > 5]
# print(lista_quadrado_maiores_5)


# temperaturas = [0, 10, 20, 30, 40]
# lista_conversao = [(temp * (9/5)) + 32 for temp in temperaturas]
# print(lista_conversao)


# palavras = ["python", "java", "javascript", "csharp", "go", "ruby"]
# lista_palavras_filtro = [palavra for palavra in palavras if len(palavra) > 4]
# print(lista_palavras_filtro)

#LAMBDA = "RECEBA"

# triplicar = lambda numero: numero * 3
# print(triplicar(5))


# soma = lambda a, b: a + b
# print(soma(10, 5))


# maior = lambda a, b: max(a, b)
# print(maior(10, 7))

#MAP = Aplicar uma função em cada elemento de uma sequência.

# numeros = [2, 4, 6, 8, 10]
# lista = list(map(lambda numero: numero ** 2, numeros))
# print(lista)

# numeros = [10, 20, 30, 40, 50]
# lista = list(map(lambda numero: numero - 5, numeros))
# print(lista)


# nomes = ["andre", "joao", "maria", "pedro"]
# lista_maiusculas = list(map(lambda palavra: palavra.upper(), nomes))
# print(lista_maiusculas)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_filtro = list(filter(lambda numero: numero % 2 == 0, numeros))
# print(lista_filtro)


# numeros = [5, 12, 3, 20, 8, 15, 2, 30]
# lista_maiores_10 = list(filter(lambda numero: numero > 10, numeros))
# print(lista_maiores_10)


# nomes = ["Ana", "Alexandre", "Joao", "Gabriela", "Leo", "Fernando"]
# lista_nomes_grandes = list(filter(lambda nome: len(nome) > 5, nomes))
# print(lista_nomes_grandes)


#MATRIZ

# #Para percorrer uma matriz
# for linha in matriz:
#     for numero in linha:
#         print(numero)


#Criando com for a matriz

# matriz = []

# for i in range(3): i → controla as LINHAS
#     linha = []

#     for j in range(3):  j → controla as COLUNAS 
#         linha.append(0)

#     matriz.append(linha)

# for linha in matriz:
#     print(linha)


# Com informações do User

# linhas = int(input("Digite a quantidade de linhas: "))
# colunas = int(input("Digite a quantidade de colunas: "))

# matriz = []

# for i in range(linhas):
#     linha = []

#     for j in range(colunas):
#         linha.append(j)

#     matriz.append(linha)

# for i in matriz:
#     print(i)


# matriz = [[i + j for j in range(3)] for i in range(3)]

# for linha in matriz:
#     print(linha)

















