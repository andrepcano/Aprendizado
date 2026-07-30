#Escreva um programa que leia dois números inteiros e compare os dois,
#Mostrando na tela uma mensagem:
#-O primeiro valor é maior!!
#_O segundo valor é maior
#-Nao existe valor maior, são iguais

numero_a = float(input("Me fale o número A e compararei com o número B e direi qual é maior: "))
numero_b = float(input("Me fale o número B e compararei com o número A e direi qual é maior: "))

if numero_a > numero_b:
    print("O número A é maior!!")
elif numero_b > numero_a:
    print("O número B é maior!!")
elif numero_a == numero_b:
    print("Os números são iguais!!")
else:
    print("Número Inválido!!")

