# -Ex.4 Solicite a idade da pessoa e retorne se ela é criança, adolescente,
# jovem adulto,adulto ou idoso.
#
# idade < 11 = criança
# idade >= 11 < 18 = adolescente
# idade >= 18 < 40 = jovem adulto
# idade >= 40 < 60 = adulto
# else (idoso)

idade = float(input("Digite sua idade: "))

if idade < 11:
    print("Você é uma criança!!")
elif idade >= 11 and idade < 18:
    print("Você é um adolescente!!")
elif idade >= 18 and idade < 40:
    print("Você é um jovem adulto!!")
elif idade >= 40 and idade < 60:
    print("Você é um adulto!!")
else:
    print("Você é um idoso!!")

