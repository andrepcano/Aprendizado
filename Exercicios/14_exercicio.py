# Exercício 14

renda_mensal = float(input("Digite sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))
renda_minima = 2000.00
parcela_maxima = (renda_mensal * 30) /100

if renda_mensal < renda_minima:
    print("Infelizmente você nao tem o direito de fazer o empréstimo")
elif parcela > parcela_maxima:
    print("Infelizmente você nao tem o direito de fazer o empréstimo pois sua parcela excede o límite!!")
else:
    print("PARABÉNS!! O empréstimo foi APROVADO!!")

