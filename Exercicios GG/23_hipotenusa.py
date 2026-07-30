#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo, calcule e mostre o comprimento da hip

import math

cat_adj = float(input("Me diga o comprimento do cateto adjacente: "))
cat_op = float(input("Me diga o comprimento do cateto oposto: "))

hip = math.sqrt(math.pow (cat_adj, 2) + math.pow (cat_op, 2))
print("A hipotenusa dos catetos {} e {} é: {}".format(cat_adj, cat_op, hip))

