#Crie um programa que vai ler vários numero e colocar em uma lista. Depois disso, mostre: 
#A)Quantos numeros foram digitados, B)A lista de valores, ordenada de forma decrescente,
#C)Se o valor 5 foi digitado e esta ou nao na lista

lista_numeros = []

while True:
    numero = int(input("Digite um número: "))
    decisao = input("Quer continuar (S/N): ").lower()
    
    lista_numeros.append(numero)
    while decisao not in ("s", "n"):
        print("Digite corretamente...")
        decisao = input("Quer continuar (S/N): ").lower()
    if decisao == "s":
        continue
    elif decisao not in ("s", "n"):
        print("Digite corretamente...")
        decisao = input("Quer continuar (S/N): ").lower()
    else:
        break
    
if 5 in lista_numeros:
    print("O valor 5 esta na lista!")
else:
    print("O valor 5 não esta na lista!")

lista_numeros.sort(reverse=True)
qntd_num = len(lista_numeros)
print(f"Foram digitados {qntd_num} numeros!")
print(f"Lista de Numeros: \n {lista_numeros}")
        






