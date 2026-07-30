#EXERCÍCIOS LAÇOS DE REPETIÇÃO
#Faça um programa que mostre na tela uma contagem regressiva 
#para o estouro de fogos de artifício, indo de 10 até 0, com
#uma pausa de 1 seg entre elas

# import time

# for c in range(10, -1, -1):
#     print("Em {}".format(c))
#     time.sleep(1)
# print("FIM")

for c in range(2, 10, 2):
    print(c)
print("FIM")


n = int(input("Digite um numero: "))
for c in range(0, n+1):
    print(c)
print("FIM")


i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("FIM")



