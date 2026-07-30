# Exercício 32

idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade >= 60:
        print("Você é idoso")
    else:
        print("Você é adulto")
elif idade >= 12:
    print("Você é adolescente!")
else:
    print("Você é criança!")

