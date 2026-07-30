# Exercício 21

numeros_contagem = [10,9,8,7,6,5,4,3,2,1,0]

for numero_contagem in numeros_contagem:
    if numero_contagem > 0 and numero_contagem %2 == 0:
        print(f"Faltam apenas {numero_contagem} segundos - Não perca essa oportunidade!")
    elif numero_contagem > 0 and numero_contagem %2 != 0:
        print(f"A contagem continua: {numero_contagem} segundos restantes.")
    else:
        print("Aproveite a promoção agora!!")
    break;

