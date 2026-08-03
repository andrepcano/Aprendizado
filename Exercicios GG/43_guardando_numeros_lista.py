#Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre
#qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista_numeros = []

for i in range(5):
    try:
        numero = int(input(f"Digite o {i + 1} numero: "))
        lista_numeros.append(numero)
    except ValueError:
        print("Digite o valor correto...")
        continue

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print("-=" * 17)

for posicao, numero in enumerate(lista_numeros):
    if numero == maior_numero:
        print(f"Maior Número: {maior_numero} na {posicao + 1} posição")
    if numero == menor_numero:
        print(f"Menor Número: {menor_numero} na {posicao + 1} posição")


