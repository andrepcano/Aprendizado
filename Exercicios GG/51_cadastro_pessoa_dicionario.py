#Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e cadastre-os,
#(com idade) em um dicionario, se por acaso o CTPS for diferente de ZERO, o dicionario recebera tambem o ano de 
#contratação e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa irá se aposentar

from datetime import datetime

pessoas = dict()

pessoas["nome"] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
pessoas["idade"] = datetime.now().year - nasc
pessoas["carteira_trabalho"] = int(input("Carteira de TRabalho (0 não tem): "))
if pessoas["carteira_trabalho"] != 0:
    pessoas["ano_contratacao"] = int(input("Ano contratação: "))
    pessoas["salario"] = float(input("Salario: R$ "))
    pessoas["idade_aposentadoria"] = pessoas["idade"] + ((pessoas["ano_contratacao"] + 35) - datetime.now().year)

print("-" * 30)
for keys, values in pessoas.items():
    print(f"{keys} tem o valor {values}")





