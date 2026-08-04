#Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras
#que vao conter apenas os valores pares e ímpares digitados, respectivamente.
#Ao final, mostre o conteudo das tres listas geradas

lista_numeros = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input("Digite um numero: "))
    decisao =  input("Quer continuar (S/N): ").lower()
    lista_numeros.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    while decisao not in ("s", "n"):
        print("Digite Corretamente...")
        decisao =  input("Quer continuar (S/N): ").lower()
    if decisao == "s":
        continue
    else:
        break


print(f"\nLista Numeros: {lista_numeros}\n")
print(f"Lista Pares: {lista_pares}\n")
print(f"Lista Impares: {lista_impares}")







