#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km(mostre uma mensagem dizendo "multado")
#A multa custará 7R$ para cada km a cima do permitido

velocidade = int(input("Qual a velocidade que seu carro passou?: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade-80) * 7
    print("Você terá que pagar uma multa de {:.2f}R$".format(multa))
print("Tenha um bom dia! Dirija com SEGURANÇA!")

