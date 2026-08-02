#Crie um programa que tenha uma tupla com varias palavras (nao usar acentos). Depois disso,
#voce deve mostra, para cada palavra quais sao suas vogais

palavras = (
    ("tampa"),
    ("canudo"),
    ("arrancada"),
    ("polia"),
    ("cadastro")
)

for palavra in palavras:
    lista_vogais = []
    for letra in palavra:
        if letra in ("a", "e", "i", "o", "u"):
            lista_vogais.append(letra)
    vogais = tuple(lista_vogais)

    print(f"Na palavra {palavra.upper()} tem as Vogais: {vogais}")
