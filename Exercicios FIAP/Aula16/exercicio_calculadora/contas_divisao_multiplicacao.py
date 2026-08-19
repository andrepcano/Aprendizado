def multiplicacao(*n):
    resultado = 1

    for i in n:
        resultado *= i

    return resultado

def divisao(*n):
    resultado = n[0]

    for i in n:
        resultado /= i

    return resultado