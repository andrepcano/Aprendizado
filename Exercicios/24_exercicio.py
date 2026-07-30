# Exercício 24

def calculo_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos!!")
calculo_idade()

