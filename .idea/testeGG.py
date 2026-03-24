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

'''import random

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
    print("Opçao Invalida")'''



#EXERCÍCIOS LAÇOS DE REPETIÇÃO

'''for c in range(2, 10, 2):
    print(c)
print("FIM")


n = int(input("Digite um numero: "))
for c in range(0, n+1):
    print(c)
print("FIM")


i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p):
    print(c)
print("FIM")



#Faça um programa que mostre na tela uma contagem regressiva 
#para o estouro de fogos de artifício, indo de 10 até 0, com
#uma pausa de 1 seg entre elas

# import time

# for c in range(10, -1, -1):
#     print("Em {}".format(c))
#     time.sleep(1)
# print("FIM")'''



#Crie um programa que mostra na tela todos os numeros pares que
#estão no intervalo entre 1 e 50

'''for c in range(49, 0, -1):
    if (c % 2 == 0):
        print(c)
print("FIM")'''



#Faça um programa que calcule a soma de todos os numeros impares
#que sao multiplos de 3 e que se encontram entre 1 ate 500.

'''soma = 0

for c in range(1, 501):
    if(c % 2 != 0):
        soma += c 
        print("Soma dos números ímpares entre 1 e 500: ", soma)
print("FIM")
'''


#Faça um programa que leia um número qualquer e mostre
#na tela a sua tabuada, utilizando um laço for

'''numero = int(input("Me dê um número e direi a tabuada: "))

for c in range(1, 11):
    resultado = (numero * c)
    print(f" {numero} x {c} = {resultado}")
print("FIM")
'''


#Desenvolva um programa que leia seis números inteiros e mostre
#a soma apenas daqueles que forem pares. Se o valor digitado for
#ímpar desconsidere-o

'''soma = 0
cont = 0

for c in range(1,7):
    numero = int(input("Digite o {} valor: ".format(c)))

    if numero % 2 == 0:
        soma += numero
        cont += 1
        print("Voce informou {} numeros e a soma foi: {}".format(cont, soma))
print("FIM")'''
    


#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão

'''cont = 0
termo_um = int(input("Me informe o primeiro termo de uma PA: "))
razao = int(input("Me informe a razão de uma PA: "))
termo_dez = termo_um + (10 - 1) * razao

for c in range (termo_um, termo_dez + razao, razao):  
    cont += 1
    print("O {} termo da PA é: {}".format(cont, c))
print("FIM")
'''


#Faça um programa que leia um número inteiro e diga se ele é
#ou não um número primo.

#DIFICIL DEMAIS
# numero = int(input("Me diga um número e direi se é inteiro: "))
# total = 0

'''for c in range(1, numero + 1):
    if (numero % c == 0):
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(c), end="")
if (total == 2):
    print("É um número primo!")
else:
    print("Não é um número primo!")
print("Número {} foi divísivel {} vezes".format(numero, total))'''



#Crie um programa que leia uma frase qualquer e diga se ela é
#um palindromo, desconsiderando os espaços

#DIFICIL DEMAIS
'''texto = input("Escreva algo e direi se é um palíndromo: ")
texto_minusculo = texto.lower()
texto_junto = ""
texto_invertido = ""

for c in texto_minusculo:
    if c != " ":
        texto_junto = texto_junto + c

for c in texto_junto:
    texto_invertido = c + texto_invertido
if texto_junto == texto_invertido:
    print("O texto {} é um palíndromo".format(texto))
else:
    print("O texto {} não é um palíndromo".format(texto))'''



#Crie um prpgrama que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas ja atingiram

'''from datetime import date

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
print("{} pessoas são menor de idade!".format(total_menor))'''



#Faça um programa que leia o peso de 5 pessoas.No final mostre
#qual foi o maior e o menor peso lidos respectivamente

'''maior_peso = 0
menor_peso = 0

for pessoa in range(1,6):
    peso = float(input("Qual peso da pessoa {}: ".format(pessoa)))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print("O maior peso lido foi de {}Kg".format(maior_peso))
print("O menor peso lido foi de {}Kg".format(menor_peso))'''



#Desenvolva um programa que leia o nome,idade,sexo de 4 pessoas
#No final do programa, mostre:
#- A média de idade do grupo
#- Qual é o nome do homem mais velho
#- Quantas mulheres tem menos de 20 anos

#FIZ GRANDE PARTE SOZINHO(MUITO LEGAL)
   
'''fem_menor = 0
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
print("{} mulheres tem menos de 20 anos".format(fem_menor))'''



#Exercícios de módulos MATH

#Ctie um programa que leia um número real qualquer e transforme em
#um número inteiro

'''import math

num = float(input("Digite um numero qualquer e transformarei em um numero inteiro: "))

print("O numero {} inteiro é {}".format(num, int(num)))'''



#Faça um programa que leia o comprimento do cateto oposto e do
#cateto adjacente de um triângulo, calcule e mostre o comprimento da hip
'''import math

cat_adj = float(input("Me diga o comprimento do cateto adjacente: "))
cat_op = float(input("Me diga o comprimento do cateto oposto: "))

hip = math.sqrt(math.pow (cat_adj, 2) + math.pow (cat_op, 2))
print("A hipotenusa dos catetos {} e {} é: {}".format(cat_adj, cat_op, hip))'''



#Faça um rpograma que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse ãngulo
'''import math

angulo = int(input("Qual ângulo você quer saber o seno,coss, e tan: "))
rad = math.radians(angulo)

seno = math.sin(rad)
coss = math.cos(rad)
tan = math.tan(rad)

print("O seno do ângulo é: {:.2f}".format(seno))
print("O cosseno do ângulo é: {:.2f}".format(coss))
print("A tângente do ângulo é: {:.2f}".format(tan))'''



#Um professor quer sortear um de seus quatro alunos para apagar
#o quadro. Faça um programa que ajude ele, lendo o nome deles e 
#escrevendo o nome do escolhido
'''from random import choice

nome_1 = input("Nome do 1 aluno: ")
nome_2 = input("Nome do 2 aluno: ")
nome_3 = input("Nome do 3 aluno: ")
nome_4 = input("Nome do 4 aluno: ")
lista = [nome_1, nome_2, nome_3, nome_4]

escolhido = choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))'''



#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia o 
#nome dos quatro alunos e msotre a ordem sorteada
'''from random import shuffle

nome_1 = input("Nome do 1 aluno: ")
nome_2 = input("Nome do 2 aluno: ")
nome_3 = input("Nome do 3 aluno: ")
nome_4 = input("Nome do 4 aluno: ")
lista = [nome_1, nome_2, nome_3, nome_4]

ordem = shuffle(lista)
print("A ordem da apresentação será:")
print(lista)'''



#Exercicios (IF, ELIF, ELSE)

#Escreva um rpograma que faça o computador escolher entre 1 e 5
# e peça para o usuário tentar descobrir qual numero foi
#o programa deve mostrar se o usuário venceu ou perdeu
'''import random

tentativa = int(input("Tente acertar o número escolhido entre 0 a 5: "))

numero = random.randint(0, 6)

if tentativa == numero:
    print("VOCÊ ACERTOU!")
else:
    print("Você ERROU")'''



#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km(mostre uma mensagem dizendo "multado")
#A multa custará 7R$ para cada km a cima do permitido

'''velocidade = int(input("Qual a velocidade que seu carro passou?: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade-80) * 7
    print("Você terá que pagar uma multa de {:.2f}R$".format(multa))
print("Tenha um bom dia! Dirija com SEGURANÇA!")
'''


#Crie um programa que leia o número inteiro e mostre na tela
#se ele é par ou ímpar

'''numero = int(input("Digite um número e direi se é par ou ímpar: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")'''



#Desenvolta um programa que pergunte a distância de uma viagem em Km
#Calcule o preço da passagem, cobrando 0,50R$ por Km para viagens até 200km
#e 0,45R$ para mais longas

'''distancia = int(input("Qual a distância da viagem em Km: "))

if distancia <= 200:
    preco = 0.50 * distancia
    print("Você terá que pagar {}R$ pela passagem:".format(preco))
else:
    preco = 0.45 * distancia
    print("Você terá que pagar {}R$ pela viagem".format(preco))'''

