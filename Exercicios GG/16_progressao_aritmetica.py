#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão

cont = 0
termo_um = int(input("Me informe o primeiro termo de uma PA: "))
razao = int(input("Me informe a razão de uma PA: "))
termo_dez = termo_um + (10 - 1) * razao

for c in range (termo_um, termo_dez + razao, razao):  
    cont += 1
    print("O {} termo da PA é: {}".format(cont, c))
print("FIM")

