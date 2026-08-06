'''ano = 2000
nome = 'Helder'
valor = 10.5
print(f"{nome:-^10s} nasceu em {ano} e comprou um salgado pelo valor de R${valor}")'''


#Ex.1
#Escreva um programa que leia 2 numeros do usuario e exiba o resultado de 2a x 3b, em que
#a é o primeiro numero e b o segundo

'''n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

resultado = (2*n1) * (3*n2)
print(f"O resultado entre 2x{n1} e 3x{n2} = {resultado}")'''


#Ex.2
#Faça um programa para printar na tela elemento a elemeno da lista (usando while)

'''lista = ["Andre", "Pedro", "Ana", "Melissa", "Luisa", "David"]

while lista'''



#Ex.3
#Pergunte ao usuario a qntd de notas desejadas para incluir em uma lista
#Crie uma lista com os valores que sera passado pelo usuario
#Printe em tela elemento a elemento da lista (usando while)
#Crie uma nova lista apenas com as notas dos alunos que passaram de ano (>=6)

'''lista_notas = []
lista_aprovados = []

n = int(input("Quantos numeros quer que a lista tenha: "))

for numero in range(n):
    while True:
        try:
            nota = float(input(f"Digite a {numero+1} nota: "))
            lista_notas.append(nota)
            break
        except ValueError:
            print("Digite corretamente...")

for numero in lista_notas:
    if numero >= 6:
        lista_aprovados.append(numero)

contador = 0
while contador < len(lista_notas):
    print(f"{contador + 1} Nota: {lista_notas[contador]}")
    contador+=1


print(f"Notas Aprovadas: {lista_aprovados}")'''


#Ex.4
#Crie um programa simulando uma pilha, com o usuario podendo escolher se quer "Lavar a Louça" ou "Adicionar una Louça"

'''louca = []

while True:
    while True:
        try:
            print(" 1- Adicionar uma Louça\n 2- Lavar uma Louça\n 3- Olhe a Ultima Louça a ser Adicionada \n 4- Quantas Louças tem\n 0- Sair")
            opcao = int(input("Escolha: "))
            break
        except ValueError:
            print("Digite Corretamente...")

    if opcao == 1:
        nome_louca = input("Nome da Louça: ")
        louca.append(nome_louca)
    elif opcao == 2:
        if len(louca) > 0:
            removida = louca.pop()
            print("Louça lavada:", removida)
        else:
          print("Não tem louça para lavar!")
    elif opcao == 3:
        print(louca[-1])
    elif opcao == 4:
        qntd_louça = len(louca)
        print(qntd_louça)
    elif opcao == 0:
        break
    else:
        print("Ocorreu um Erro...")'''



#Ex.5
#Defina a função matematica da figura na lousa:
#Retorne o valor de y(x) dado a entrada do valor x pelo usuario




        



