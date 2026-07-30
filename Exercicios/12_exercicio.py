# Exercício 12

distancia_percorrida = float(input("Digite o total de distância percorida em (Km): "))

if distancia_percorrida <= 100:
    print("O valor total de passagem será de R$: 10.00!!")
elif 100 < distancia_percorrida <= 200:
    print("O valor total de passagem será de R$: 20.00!!")
else:
    print("O valor total de passagem será de R$: 30.00!!")

