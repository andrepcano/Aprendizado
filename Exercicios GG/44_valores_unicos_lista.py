#Crie um programa onde o ususario pode digitar varios valores numericos e cadastre-os em uma lista
#Caso o número ja exista la dentro, ele não sera adicionado. No final, serão exibidos todos os valores unicos
#digitados, em ordem crescente

lista_numeros = []

n = int(input("Quantos números quer digitar: "))

for i in range(n):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1} numero: "))
            break
        except ValueError:
            print("Digite apenas números inteiros...")
    if numero not in lista_numeros:
        lista_numeros.append(numero)

lista_numeros.sort()
print(f"Lista Completa em Ordem Crescente: {lista_numeros}")








