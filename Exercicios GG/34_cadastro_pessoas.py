#Crie um programa que leia a idade e o sexo de pessoas, a cada pessoa cadastrada, o programa deve perguntar
#se o usuário quer continuar, No final mostre: A) quantas pessoas tem mais de 18 anos, B) quantos homens foram cadastrados
#C) quantas mulheres tem menos de 20 anos

qntd_cadastro = 1
maior_idade = 0
sexo_masc = 0
sexo_fem = 0
fem_menos_de_20 = 0

while True:
    print(f"Cadastro {qntd_cadastro}")
    qntd_cadastro += 1
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Digite um valor correto!")
        continue

    sexo = input("Digite seu sexo (masc) (fem): ").lower()
    if sexo not in ("masc", "fem"):
        print("Escreva da maneira correta!")
        continue
    else:
        if sexo == "masc":
            sexo_masc += 1
        else:
            sexo_fem += 1
    
    if idade > 18:
        maior_idade += 1

    if idade < 20 and sexo == "fem":
        fem_menos_de_20 += 1

    decisao = input("Quer continuar cadastrando? (s) ou (n): ").lower()
    while decisao not in ("s", "n"):
        print("Digite corretamente!")
        decisao = input("Quer continuar cadastrando? (s) ou (n): ").lower()

    if decisao == "n":
        print(f"Quantidade de pessoas com mais de 18 anos {maior_idade}")
        print(f"Quantidade de homens cadastrados {sexo_masc}")
        print(f"Quantidade de mulheres com menos de 20 anos {fem_menos_de_20}")
        break


