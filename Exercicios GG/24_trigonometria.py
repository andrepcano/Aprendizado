#Faça um rpograma que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ãngulo

import math

angulo = int(input("Qual ângulo você quer saber o seno,coss, e tan: "))
rad = math.radians(angulo)

seno = math.sin(rad)
coss = math.cos(rad)
tan = math.tan(rad)

print("O seno do ângulo é: {:.2f}".format(seno))
print("O cosseno do ângulo é: {:.2f}".format(coss))
print("A tângente do ângulo é: {:.2f}".format(tan))

