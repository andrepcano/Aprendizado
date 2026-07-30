#Faça um programa que leia um número inteiro e diga se ele é
#ou não um número primo.

#DIFICIL DEMAIS
# numero = int(input("Me diga um número e direi se é inteiro: "))
# total = 0

for c in range(1, numero + 1):
    if (numero % c == 0):
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
if (total == 2):
    print("É um número primo!")
else:
    print("Não é um número primo!")
print("Número {} foi divísivel {} vezes".format(numero, total))

