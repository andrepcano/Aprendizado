'''-Ex.1 Solicite para o usuário o salario 
e retorne o respectivo desconto e valor a ser recebido em funçao da tabela de descontos do Brasil'''

'''Salário de Contribuição (R$) 	Alíquota progressiva para fins de recolhimento ao INSS
Até R$ 1.621,00	7,5%
De R$ 1.621,01 a R$ 2.902,84	9%
De R$ 2.902,85 até R$ 4.354,27	12%
De R$ 4.354,28 até R$ 8.475,55	 14%'''

'''salario = float(input("Digite o seu salário: "))
if salario <= 1621.00:
    desconto = (salario * 7.5) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
elif 1621.01 <= salario <= 2902.84:
    desconto = (salario * 9) /100
    print(f"O desconto do INSS é de R$: {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
elif 2902.85 <= salario <= 4354.27:
    desconto = (salario * 12) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
else:
    desconto = (salario * 14) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")'''




'''-Ex.2 Crie um algoritmo para solicitar o salario recebido durante o mes
 e calcule o imposto a ser pago, bem como o salario a receber

 salario = input for user
 imposto = 15%'''

'''salario = float(input("Digite seu salario: "))
imposto = (salario * 15) /100

print(f"O imposto a ser descontado do seu salario é de R$ {imposto:.2f}")
print(f"O valor a ser recebido ja com o imposto descontado é de R$ {salario - imposto:.2f}")'''




'''-Ex.3 Solicite o salario do usuario é descubra o quanto de aumento teve'''

'''salario_antigo = float(input("Qual era seu salário: "))
aumento = float(input("Quantos porcento de aumento você teve: "))

salario_atual = (salario_antigo * aumento) /100
print(f"O valor do aumento no seu salário é deR$: {salario_atual:.2f}")
print(f"O valor total do seu salário atual é de R$ {salario_antigo + salario_atual:.2f}")'''




'''-Ex.4 Solicite a idade da pessoa e retorne se ela é criança, adolescente,
jovem adulto,adulto ou idoso.

idade < 11 = criança
idade >= 11 < 18 = adolescente
idade >= 18 < 40 = jovem adulto
idade >= 40 < 60 = adulto
else (idoso)'''

'''idade = float(input("Digite sua idade: "))

if idade < 11:
    print("Você é uma criança!!")
elif idade >= 11 and idade < 18:
    print("Você é um adolescente!!")
elif idade >= 18 and idade < 40:
    print("Você é um jovem adulto!!")
elif idade >= 40 and idade < 60:
    print("Você é um adulto!!")
else:
    print("Você é um idoso!!")'''

#EXERCÍCIOS DE CONDIÇÕES (IF,ELIF AND ELSE)

'''quantidade_macas_vendidas = int(input("Quantas maças foram vendidas: "))
quantidade_bananas_vendidas = int(input("Quantas bananas foram vendidas: "))

if quantidade_macas_vendidas > quantidade_bananas_vendidas:
    print(f"A quantidade de maças vendidas é maior que a quantidade de bananas vendidas!!")
elif quantidade_bananas_vendidas > quantidade_macas_vendidas:
    print(f"A quantidade de bananas vendidas é maior que a quantidade de maças vendidas!!")
else:
    print(f"A quantidade de maças vendidas é igual a de bananas vendidas!!")'''




'''atividade_a = int(input("Digite o tempo gasto na atividade A: "))
atividade_b = int(input("Digite o tempo gasto na atividade B: "))
atividade_c = int(input("Digite o tempo gasto na atividade C: "))

if atividade_a + atividade_b + atividade_c > 0:
    print(f"O tempo total gasto nas atividades é de {atividade_a + atividade_b + atividade_c} dias!!")
else:
    print("ERRO!! os dias nao podem ser negativos!!")'''



'''temperatura_atual = float(input("Qual a temperatura atual em Celsius do servidor: "))
temperatura_maxima = 25.0

if temperatura_atual > temperatura_maxima:
    print("ALERTA!! Limite acima do permitido!!!")
else:
    print("Temperatura dentro do limite permitido!!")'''




'''peso = float(input("Digite seu peso atual em (Kg): "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura **2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f} e você está abaixo do peso!!")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de {imc:.2f} e você está com o peso normal!!")
else:
    print(f"Seu IMC é de {imc:.2f} e você está ACIMA do peso!!")'''




'''total_despesas = float(input("Digite o total de despesas do mês R$: "))
orcamento = 3000.00

if total_despesas > orcamento:
    print("ALERTA!! Suas despesas estão acima do seu orçamento!!")
else:
    print("Suas despesas estão dentro do limite estabelecido!!")'''




'''hora_atual = float(input("Qual o horário atual: "))
horario_maximo = 17.59
horario_minimo = 8.00

if hora_atual > horario_maximo or hora_atual < horario_minimo:
    print("VOCÊ NÃO PODE ENTRAR AQUI ESSE HORÁRIO!!!!!!!")
else:
    print("Acesso Liberado!!!")
    print("Seja Bem Vindo!!!")'''




'''nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))

media = (nota_um + nota_dois + nota_tres) /3

if media >= 7.0:
    print(f"Sua média é de {media:.2f} e você esta APROVADO!!")
elif 5 <= media < 7.0:
    print(f"Sua média é de {media:.2f} e você esta de RECUPERAÇÃO!!")
else:
    print(f"Sua média é de {media:.2f} e você esta REPROVADO!!")'''




'''distancia_percorrida = float(input("Digite o total de distância percorida em (Km): "))

if distancia_percorrida <= 100:
    print("O valor total de passagem será de R$: 10.00!!")
elif 100 < distancia_percorrida <= 200:
    print("O valor total de passagem será de R$: 20.00!!")
else:
    print("O valor total de passagem será de R$: 30.00!!")'''




'''numero = int(input("Digite um número inteiro e direi se é par ou ímpar: "))
par = numero %2 == 0
impar = numero %2 != 0

if par:
    print(f"O número {numero} é PAR!!")
else:
    print(f"O número {numero} é IMPAR!!")'''




'''renda_mensal = float(input("Digite sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))
renda_minima = 2000.00
parcela_maxima = (renda_mensal * 30) /100

if renda_mensal < renda_minima:
    print("Infelizmente você nao tem o direito de fazer o empréstimo")
elif parcela > parcela_maxima:
    print("Infelizmente você nao tem o direito de fazer o empréstimo pois sua parcela excede o límite!!")
else:
    print("PARABÉNS!! O empréstimo foi APROVADO!!")'''

#FIM EXERCÍCIOS DE CONDIÇÕES (IF,ELIF AND ELSE)

#EXERCÍCIOS DE LAÇOS DE REPETIÇÃO (FOR AND WHILE)

'''clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(f"Ola {cliente}, seja bem vindo a nossa loja!!")
    range(4)'''



'''contador = 0

while contador < 5:
    print("Bem-vindo ao Buscante!")
    contador += 1
    break;'''




'''valores = [10, 20, 30, 40, 50]

for valor in valores:
    total_soma = sum(valores)
    print(f"A soma total dos valores é de R$: {total_soma:.2f}")
    break;'''


 

'''projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print(f"Valor Ausente")
    else:
         print(projeto)'''




'''livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"O livro {livro} é um clássico da literatura de fantasia!!!")
        break;'''




'''estoques = [{'livro': '1984', 'quantidade': 1},
    {'livro': 'Dom Casmurro', 'quantidade': 32}]

for estoque in estoques:
    if estoque['quantidade'] > 0:
        print(f"Livro disponível: {estoque['livro']}")

compra = input(f"Você deseja comprar qual livro: ")

for estoque in estoques:
    if estoque ['livro'] == compra and estoque['quantidade'] > 0:
        estoque["quantidade"] -= 1
        print(f"Parabéns pela compra do livro: {estoque['livro']} ")
        print(f"Quantidade atual: {estoque['quantidade']}")
        break;
    else:
        print("Desculpe, Livro Esgotado!!")'''




'''numeros_contagem = [10,9,8,7,6,5,4,3,2,1,0]

for numero_contagem in numeros_contagem:
    if numero_contagem > 0 and numero_contagem %2 == 0:
        print(f"Faltam apenas {numero_contagem} segundos - Não perca essa oportunidade!")
    elif numero_contagem > 0 and numero_contagem %2 != 0:
        print(f"A contagem continua: {numero_contagem} segundos restantes.")
    else:
        print("Aproveite a promoção agora!!")
    break;'''




'''livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro['estoque'] > 0:
        print(f"O livro {livro['nome']} está disponível!!")'''




'''while True:
    nome_user = input("Digite seu nome de usuário: ")
    senha_user = input("Digite sua senha: ")

    if len(nome_user) < 5:
        print("O nome de usuário deve conter pelo menos 5 caractéres!!")
        continue
    elif len(senha_user) < 8:
        print("A senha deve conter pelo menos 8 caractéres!!")
        continue
    print("Cadastro realizado com Sucesso!!")
    break;'''

#FIM EXERCÍCIO LAÇOS DE REPETIÇÃO (FOR AND WHILE)


#INÍCIO EXERCÍCIOS DE FUNÇÕES (DEF)

'''def calculo_idade():
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos!!")
calculo_idade()'''



'''def contar_caracteres(palavra):
    palavra = input("Digite uma palavra e contarei quantos caracteres ela tem: ")
    quantidade_caracteres = len(palavra)
    print(f"A palavra {palavra} tem {quantidade_caracteres} caracteres!!")
contar_caracteres('palavra')'''



'''def saudaçao_personalizada(hora_dia):

    if hora_dia < 12:
        return "Bom Dia!!"
    elif 12 <= hora_dia < 18:
        return "Boa Tarde!!"
    else:
        return "Boa Noite!!"

hora_atual = float(input("Qual o horario atual(0-23): "))
print(saudaçao_personalizada(hora_atual))'''



'''def convercao(lista):
    return [int (telefone) for (telefone) in lista]

def confirmar_tipos(lista):

    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversão"
        
    return "Todos os números foram convertidos corretamente!"

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = convercao(telefones)
print(confirmar_tipos(telefones_convertidos))'''

'''def area(larg, com):
    resultado_area = larg * com
    print(f"O resultado da área do retângulo é: {resultado_area}")

l = float(input("Me informa a largura e comprimento do retângulo: " ))
c = float(input("Digite o comprimento do retângulo: "))
area(l, c)'''



'''def escreva(palavra):
    print("-" * 30)
    print(palavra)
    print("-" * 30)


p = input("Digite uma palavra: ")
escreva(p)'''



'''def contador(inicio, fim, passo):
    while (passo >= 0 and inicio <=fim) or (passo < 0 and inicio >= fim):
        print(inicio)
        inicio += passo


contador(0, 10, 1)
contador(10, 0, -1)

print("Agora é a sua vez de aumentar a contagem!!")
i = int(input("Digite o número de início: "))
f = int(input("Digite o número do fim: "))
p = int(input("Digite o número do passo: "))
contador(i, f, p)'''





