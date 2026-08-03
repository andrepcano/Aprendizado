#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista
#ja na posição correta de inserção(sem usar o sort()). No final. mostre a lista ordenada no terminal.

lista_numeros = []

for i in range(5):
    while True:
        try:
            numeros = int(input(f"Digite o {i + 1} numero: "))
            break
        except ValueError:
            print("Digite um valor inteiro...")

    inserido = False
    for indice, valor in enumerate(lista_numeros):
        if numeros < valor:
            lista_numeros.insert(indice, numeros)
            inserido = True
            break
    if not inserido:
        lista_numeros.append(numeros)

print(lista_numeros)



