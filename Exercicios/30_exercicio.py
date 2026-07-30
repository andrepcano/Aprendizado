# Exercício 30

def contador(inicio, fim, passo):
    while (passo >= 0 and inicio <=fim) or (passo < 0 and inicio >= fim):
        print(inicio)
        inicio += passo


contador(0, 10, 1)
contador(10, 0, -1)

print("Agora é a sua vez de aumentar a contagem!!")
i = int(input("Digite o número de início: "))
f = int(input("Digite o número do fim: "))
p = int(input("Digite o número do passo: "))
contador(i, f, p)

