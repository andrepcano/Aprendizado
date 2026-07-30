#Desenvolta um programa que pergunte a distância de uma viagem em Km
#Calcule o preço da passagem, cobrando 0,50R$ por Km para viagens até 200km
#e 0,45R$ para mais longas

distancia = int(input("Qual a distância da viagem em Km: "))

if distancia <= 200:
    preco = 0.50 * distancia
    print("Você terá que pagar {}R$ pela passagem:".format(preco))
else:
    preco = 0.45 * distancia
    print("Você terá que pagar {}R$ pela viagem".format(preco))

