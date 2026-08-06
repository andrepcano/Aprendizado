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

'''def y(x):
    if x <= 2:
        res = x
    elif x<= 3.5:
        res = 2
    elif x <= 5:
        res = 3
    else:
        res = x**2 - 10*x + 28
    return res

print(y(4))'''


#Ex.6
#Crie um programa em Python que permita cadastrar alunos, registrar duas notas e calcular informaçoes da turma.
#O Programa deve permitir: 1) Cadastrar aluno (nome + 2 notas), 2) Listar todos os alunos cadastrados
#3) mostrar estatisticas da turma (total de alunos, media, aprovados/reprovados) 4) Sair do Programa
#Crie 3 listas: nomes, notas1, notas2 Funções: exibir_menu(), cadastrar_aluno(nomes, nota1, nota2)
#situacao(media), listar_alunos(nomes, nota1, nota2), estatisticas_turma(nomes, notas1, notas2)
        
lista_alunos = []
lista_nota_1 = []
lista_nota_2 = []

def escolher_opcao():
    while True:
        try:
            print(" 1- Cadastrar Alunos\n 2- Listar Alunos\n 3- Estatisticas da Turma\n 4- Sair do Programa ")
            escolha = int(input("Escolha: "))
            if escolha in (1, 2, 3, 4):
                return escolha
            else:
                print("Escolha uma opção de 1 a 4.")
                continue
        except ValueError:
            print("Digite o Número corretamente...")
            continue


while True:
    escolha = escolher_opcao()
    if escolha == 1:
        while True:
            try:
                nome = input("\nDigite o Nome: ")
                nota1 = float(input("Digite a Primeira nota: "))
                nota2 = float(input("Digite a Segunda nota: "))
                if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                    lista_alunos.append(nome)
                    lista_nota_1.append(nota1)
                    lista_nota_2.append(nota2)
                    break
                else:
                    print("As notas devem estar entre 0 e 10.")
            except ValueError:
                print("Digite o Valor corretamente...")
                continue

    elif escolha == 2:
        for indice, nome in enumerate(lista_alunos, start=1):
            print(f"{indice}° Nome: {nome}")
    elif escolha == 3:
        total_alunos = len(lista_alunos)
        print(f"\nTotal de Alunos: {total_alunos}")
        if total_alunos > 0:
            soma_notas = 0
            quantidade_notas = 0
            for nota in lista_nota_1:
                soma_notas += nota
                quantidade_notas += 1
            for nota in lista_nota_2:
                soma_notas += nota
                quantidade_notas += 1
            media_geral = soma_notas / quantidade_notas
            print(f"Media Geral: {media_geral:.1f}")
        else:
            print("Nenhum aluno cadastrado para calcular a media geral.")
        for indice, nome in enumerate(lista_alunos):
            media_aluno = (lista_nota_1[indice] + lista_nota_2[indice]) / 2
            print(f"\nMedia Aluno {indice + 1}°: {media_aluno}")
            if media_aluno >= 6:
                print("E Está APROVADO!!")
            else:
                print("E Está REPROVADO!!")
    elif escolha == 4:
        print("\nPrograma Encerrado")
        break
    






