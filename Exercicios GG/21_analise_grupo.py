#Desenvolva um programa que leia o nome,idade,sexo de 4 pessoas
#No final do programa, mostre:
#- A média de idade do grupo
#- Qual é o nome do homem mais velho
#- Quantas mulheres tem menos de 20 anos

#FIZ GRANDE PARTE SOZINHO(MUITO LEGAL)

fem_menor = 0
idade_masc = 0
nome_masc_velho = ""
soma_idade = 0

for pessoa in range(1,5):
    nome = input("Digite o nome da {} pessoa: ".format(pessoa))
    idade = int(input("Digite s idade da {} pessoa: ".format(pessoa)))
    sexo = input("Digite (M) para masculino e (F) para para identificar o sexo da {} pessoa : ".format(pessoa))
    
    soma_idade += idade
    
    if sexo =="M":
        idade_masc = idade
        nome_masc_velho = nome
    if sexo == "F":
        if idade < 20:
            fem_menor += 1

media = soma_idade / 4
    

print("A média de idade do grupo é {} anos".format(media))
print("A Homem mais velho é o {} com {} anos".format(nome_masc_velho, idade_masc))
print("{} mulheres tem menos de 20 anos".format(fem_menor))

