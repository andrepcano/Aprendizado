#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#O programa deve perguntar o salário, valor da casa, e quantas parcelas deseja pagar.
#O valor da prestação nao pode exceder de 30% do salário ou então o empréstimo será negado.

'''salario = float(input("Qual seu salário: "))
valor_casa = float(input("Qual o valor da casa que deseja comprar: "))
parcelas = float(input("Em quantas parcelas(meses) deseja pagar: "))

parcela_valor = valor_casa / parcelas
limite = (salario * 30) /100

if parcela_valor > limite:
    print("Emprestimo negado!!!")
elif parcela_valor < limite:
    print("Emprestimo aprovado!!!")
else:
    print("Emprestimo negado!!!")

print(f"o valor da prestação é de R$: {parcela_valor:.2f}")'''



#Escreva um programa que leia um número inteiro qualquer.
#E peça para o usuário escolher qual será a base da conversão.
#-1 para bínario
#-2 para octal
#-3 para hexadecimal

'''numero = int(input("Digite um número e terá três opções de conversão: "))

print("-1 Converter para Binário")
print("-2 Converter para Octal")
print("-3 Converter para Hexadecimal")
opcao = int(input("Qual opção deseja escolher(1 a 3): "))

def opcoes(numero, opcao):
    if opcao == 1:
        binario = bin(numero)[2:]
        print(f"O núemro convertido para binário da: {binario}")
    elif opcao == 2:
        octal = oct(numero)[2:]
        print(f"O número convertido para octal da: {octal}")
    elif opcao == 3:
        hexadecimal = hex(numero)[2:]
        print(f"O núemro convertido para hexadecimal da: {hexadecimal}")
    else:
        print("Opção Inválida!!")

   
opcoes(numero, opcao)'''



#Escreva um programa que leia dois números inteiros e compare os dois,
#Mostrando na tela uma mensagem:
#-O primeiro valor é maior!!
#_O segundo valor é maior
#-Nao existe valor maior, são iguais

'''numero_a = float(input("Me fale o número A e compararei com o número B e direi qual é maior: "))
numero_b = float(input("Me fale o número B e compararei com o número A e direi qual é maior: "))

if numero_a > numero_b:
    print("O número A é maior!!")
elif numero_b > numero_a:
    print("O número B é maior!!")
elif numero_a == numero_b:
    print("Os números são iguais!!")
else:
    print("Número Inválido!!")'''



#Faça um programa que leia o ano de nascimento de um jovem.
#E informe, de acordo com sua idade.
#-Se ele ainda vai se alistar no exército.
#-Se é a hora de se alistar no exército.
#-Se já passou o tempo de se alsitar.
#O programa tambem devera mostrar o tempo restante


'''ano_nascimento = int(input("Qual seu ano de nascimento: "))
ano_atual = 2026
limite = 18
resultado_ano = ano_atual - ano_nascimento

if resultado_ano < limite:
    print("Ainda vai se alistar")
    tempo_restante = limite - resultado_ano
    print(f"Falta {tempo_restante} anos para se alistar!")
elif resultado_ano == limite:
    print("Está no ANO do alistamento não perca!!")
else: 
    print("VISH!!! Ja passou o tempo do alistamento!!")'''



#Crie um programa que leia duas notas 
#de um aluno e calcule sua média, mostrando uma mensagem no final.
#de acordo com a média atingida.


'''nota_1 = float(input("Digite sua nota 1: "))
nota_2 = float(input("Digite sua nota 2: "))
nota_3 = float(input("Digite sua nota 3: "))
media = (nota_1 + nota_2 + nota_3) / 3

if media < 5.0:
    print(f"A sua média foi de {media:.2f} e você está REPROVADO!")
elif media >= 5 and media <= 6.9:
    print(f"A sua média foi de {media:.2f} e você está de RECUPERAÇÃO!")
else:
    print(f"Sua nota foi de {media:.2f} e você está APROVADO!!")'''



#A confederação nacional de natação precisa de um programa que leia o ano
#de nascimento de um atleta e mostre sua categoria conforme a idade:
#ate 9 anos: mirim
#ate 14 anos: infantil
#ata 19 anos: juniot
#ate 20 anos> sênior
#acima: mastes

'''idade = int(input("Qual a sua idade e direi qual categoria es: "))

if idade <= 9:
    print(f"Categoria mirim {idade}")
elif idade > 9 and idade <= 14:
    print(f"Categoria infantil {idade}")
elif idade > 14 and idade <= 19:
    print(f"Categoria junior {idade}")
elif idade > 19 and idade == 20:
    print(f"Categoria sênior {idade}")
else:
    print(f"Você é da categoria MASTER e tem {idade} anos")'''



#Desafio triângulos, acrescentando o recurso de mostrar que tipo de 
#triãngulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

'''seg_um = float(input("Digite o tamanho do segmento 1: "))
seg_dois = float(input("Digite o tamanho do segmento 2: "))
seg_tres = float(input("Digite o tamanho do segmento 3: "))


if seg_um < seg_tres + seg_dois or seg_dois < seg_tres + seg_um or seg_tres < seg_dois + seg_um:
    print("Pode formar um triângulo ", end='')
    if seg_um == seg_tres and seg_tres == seg_dois:
        print("EQUILÁTERO")
    if seg_tres == seg_dois != seg_um or seg_um == seg_dois != seg_tres or seg_tres == seg_um != seg_dois :
        print("ISÓSCELES")
    if seg_dois != seg_tres != seg_um:
        print("ESCALENO")
else: 
    print("Não da para formar um triângulo")'''



#Desenvolva um logica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu resultado, de acordo com a tabela
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#Entre 25 a 30: Sobrepeso
#Entre 30 ate 40: Obesidade
#Acima de 40: Obesidade Mórbida


'''altura = float(input("Qual a sua altura em (M): "))
peso = float(input("Qual seu pesoem (Kg): "))
imc = peso / altura**2

if imc < 18.5:
    print(f"Seu IMC é {imc} e você está ABAIXO do peso")
elif 18.5 < imc < 25:
    print(f"Seu IMC é {imc} e você está com o peso IDEAL")
elif 25 < imc < 30:
    print(f"Seu IMC é {imc} e você esta com SOBREPESO")
elif 30 < imc < 40:
    print(f"Seu IMC é {imc} e você está com OBESIDADE")
else:
    print(f"Seu IMC é {imc} e esta com OBESIDADE MÓRBIDA")'''



#Elabore um programa que calcule o valor a ser pago por
#um produto, considerando o seu preço normal + condição de pagamento
#A vista dinheiro/cheque: 10% de desconto
#A vsitra cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no crtão: 20% de juros

'''produto = input("Qual o nome do produto: ")
preco_normal = float(input("Digite o preço normal do produto: "))
condicao_pagamento = int(input("Condição de Pagamento: \n" \
                                "1- A vista dinheiro/cheque\n" \
                                "2- A vista cartão\n" \
                                "3- Em ate 2x no cartão\n" \
                                "4- Em 3x ou mais.\n"))

avista_cartao = (preco_normal *5) / 100
avista_normal = (preco_normal * 10) / 100
duas_vezes = preco_normal
tres_vezes_mais = preco_normal / 20  

resultado_avista_cartao = preco_normal - avista_cartao
resultado_avista_normal = preco_normal - avista_normal
resultado_tres_vezes = preco_normal + tres_vezes_mais

if condicao_pagamento == 1:
    print(f"O preço do desconto é {avista_normal}")
    print(f"O preço com desconto é {resultado_avista_normal}")
elif condicao_pagamento == 2:
    print(f"O preço do desconto é {avista_cartao}")
    print(f"O preço com desconto é {resultado_avista_cartao}")
elif condicao_pagamento == 3:
    print(f"O preço é o mesmo")
else:
    print(f"O preço do juros é {tres_vezes_mais}")
    print(f"O preço ja com juros é {resultado_tres_vezes}")'''    



#PEDRA, PAPEL OU TESOURA

import random

jogadas = ['pedra', 'papel', 'tesoura']

computador = random.choice(jogadas)

print("Vamos Jogar pedra,papel ou tesoura")
jogada = input("Escolha entre pedra, papel ou tesoura: ")
print(f"computador escolheu {computador}")

if jogada == computador:
    print("EMPATE")
elif (jogada == 'pedra' and computador == 'tesoura') or \
    (jogada == 'papel' and computador == 'pedra') or \
    (jogada == 'tesoura' and computador == 'papel'):
    print("O jogador ganhou do computador!!")
elif (jogada == 'pedra' and computador == 'papel') or \
    (jogada == 'papel' and computador == 'tesoura') or \
    (jogada == 'tesoura' and computador == 'pedra'):
    print("O computador ganhou do jogador!!")
else:
    print("Opçao Invalida")





