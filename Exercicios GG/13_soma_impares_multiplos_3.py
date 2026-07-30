#Faça um programa que calcule a soma de todos os numeros impares
#que sao multiplos de 3 e que se encontram entre 1 ate 500.

soma = 0

for c in range(1, 501):
    if(c % 2 != 0):
        soma += c 
        print("Soma dos números ímpares entre 1 e 500: ", soma)
print("FIM")

