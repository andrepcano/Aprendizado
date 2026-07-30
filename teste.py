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



#1 - Sistema de login com nível de acesso. solicite usuário e senha. Se usuário é igual a admin, 
#crie uma estrutura de condição aninhada para solicitar senha e se a mesma for '1234', mostre que 
#o usuário terá acesso total. Caso o usuário insira a senha incorreta, mostre senha incorreta. 
#Caso usuário insira usuário incorreto, mostre usuário incorreto. 
'''usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "1234":
        print("ACESSO TOTAL")
    else:
        print("Senha incorreta!")
else:
    print("Usuário incorreto!")'''




#2. Classificação de idade. solicite idade, se idade for maior ou igual a 18, crie uma estrutura de 
#alinhada para verificar se idade é maior ou igual a 60, se for, mostre que é idoso, senão, mostre 
#que é adulto. Se idade for maior ou igual a 12, adolescente, caso contrário, criança. 

'''idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade >= 60:
        print("Você é idoso")
    else:
        print("Você é adulto")
elif idade >= 12:
    print("Você é adolescente!")
else:
    print("Você é criança!")
    '''
    


#3. Aprovação com distinção. solicite nota, se nota for maior ou igual a 6, crie condição aninhada 
#para verificar se nota é maior ou igual a 9, se for aprovado com excelência. 
#e nota não for maior ou igual a 9, Aprovado. Caso contrário, reprovado. 

'''nota = float(input("Qual foi sua nota: "))

if nota >= 6:
    if nota >= 9:
        print("Aprovado com EXCELÊCIA!")
    else:
        print("Aprovado!")
else:
    print("Reprovado!")'''




#4. Verificação de número. Solicite número e verifique se é maior do que zero, se for, 
#crie uma estrutura de condição aninhada para verificar se este número é par, se for, 
#print positivo e par. Se não for, Positivo e ímpar. Se número for igual a zero, print zero,
#caso contrário negativo. 

'''numero = float(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar")
elif numero == 0:
    print("O número é 0!")
else:
    print("O número é NEGATIVO!")
'''



#5. Sistema de desconto. solicite valor e se a pessoa é vip ou não. Se valor maior ou igual 200, 
#crie estrutura de condição aninhada para verificar se a pessoa é vip, se for, 
#ofereça 20% de desconto sobre o valor e mostre o valor a ser descontado e o valor final, 
#considerando o desconto. Se não for vip, ofereça o desconto de 10%. 

'''valor = float(input("Digite um valor: "))
pessoa = input("Você é VIP (Sim) ou (Não): ").lower()

if valor >= 1000:
    if pessoa == "sim":
        desconto_vip = valor /20
        valor_desconto_vip = valor - desconto_vip
        print("Você te direito a 20% de desconto, o desconto fica de {}R$ e o valor final é {}R$".format(desconto_vip, valor_desconto_vip))
else:
    desconto_sem_vip = valor / 10
    valor_desconto = valor - desconto_sem_vip
    print("Você tem direito a 10% de desconto, o desconto fica de {}R$ e o valor final é {}R$".format(desconto_sem_vip, valor_desconto))'''




#6. Crie um algoritmo para perguntar para o usuário qual o dia da semana, caso seja sábado, 
#escreva dia de festa. Caso seja, domingo, pergunte sobre a condição física do usuário, 
#se estiver com dores de cabeça, print recuperando, então, precisa descansar. Caso contrário, 
#apenas descanse. Caso não seja sábado ou domingo, mostre trabalhando, trabalhando e trabalhando! 

'''dia_semana = input("Qual o dia da semana: ").lower()

if dia_semana == "sabado":
    print("Dia de festa!")

elif dia_semana == "domingo":
    condicao_fisica = input("Qual sua condição física: ")
    if condicao_fisica == "dores de cabeça":
        print("Recuperando, então precisa descansar!")
    else:
        print("Apenas descanse!")
else:
    print("Trabalho, trabalho, trabalho!!!")
'''



#Calculadora na qual eu errei porque não mudei 1 linha de lugar...
#Muito triste isso, mas enfim, aqui está a correção do código da calculadora:

'''valor_um = float(input("Digite um valor: "))
valor_dois = float(input("
soma = valor_um + valor_dois
subtracao = valor_um - valor_dois
multiplicacao = valor_um * valor_dois

escolha = input("Escolha se quer fazer uma (soma), (subtração), (divisão), (multiplicacao): ").lower()

if escolha == 'divisão':
    if valor_dois == 0:
        print("ERRO!")
    else:
        divisao = valor_um / valor_dois
        print("O resultado da divisão é: {}".format(divisao))
elif escolha == 'soma':
     print("A soma dos números é: {}".format(soma))
elif escolha == 'subtracao':
    print("A subtração dos números é: {}".format(subtracao))
elif escolha == 'multiplicação':
    print("A multiplicação dos números é: {}".format(multiplicacao))
else:
    print("Escolha Inválida!")Digite um valor: "))'''



#
