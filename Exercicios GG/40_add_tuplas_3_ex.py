#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9, B)Em que posição foi digitado o primeiro valor tres, C)Quais foram os números pares

lista = []
lista_pares = []
qntd_nove = 0
posicao_tres = 0

for i in range(4):
    numeros = int(input(f"Digite o {i + 1} valor: "))
    lista.append(numeros)
    #C
    if numeros % 2 == 0:
        lista_pares.append(numeros)

valores = tuple(lista)
valores_par = tuple(lista_pares)

#A) e B)
for i in valores:
    if i == 9:
        qntd_nove += 1
    elif 3 in valores:
        posicao_tres = valores.index(3) + 1
    else:
        continue

print(f"Você digitou os valores: {valores}")
print(f"O valor 9 apareceu {qntd_nove} vezes")
if posicao_tres >= 1:
    print(f"O numero 3 foi digitado a primeira vez na {posicao_tres} posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print(f"Os números pares foram os {valores_par}")

