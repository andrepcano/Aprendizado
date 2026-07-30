#Crie um prpgrama que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas ja atingiram

from datetime import date

total_maior = 0
total_menor = 0
ano_atual = date.today().year
for pessoas in range(1, 8):
    ano_nascimento = int(input("Em que ano a {} pessoa nasceu: ".format(pessoas)))
    idade = ano_atual - ano_nascimento
    print("Essa pessoa tem {} anos".format(idade))

    if idade >= 21:
        print("A pessoa {} que tem {} anos é maior de idade!".format(pessoas, idade))
        total_maior += 1
    else:
        print("A pessoa {} que tem {} anos é menor de idade!".format(pessoas, idade))
        (total_menor) += 1
print("{} pessoas são Maior de idade!".format(total_maior))
print("{} pessoas são menor de idade!".format(total_menor))

