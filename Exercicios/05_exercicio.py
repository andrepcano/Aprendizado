# Exercício 5

quantidade_macas_vendidas = int(input("Quantas maças foram vendidas: "))
quantidade_bananas_vendidas = int(input("Quantas bananas foram vendidas: "))

if quantidade_macas_vendidas > quantidade_bananas_vendidas:
    print(f"A quantidade de maças vendidas é maior que a quantidade de bananas vendidas!!")
elif quantidade_bananas_vendidas > quantidade_macas_vendidas:
    print(f"A quantidade de bananas vendidas é maior que a quantidade de maças vendidas!!")
else:
    print(f"A quantidade de maças vendidas é igual a de bananas vendidas!!")

