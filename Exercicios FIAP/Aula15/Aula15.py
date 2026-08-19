#Ex.1
'''def soma(*args):
    total = 0
    for nota in args:
        total += nota
    return f"Soma total: {total:.1f}"

#OU
#def soma(*args):
#   return sum(args)

print(soma(2,3,4,5))'''

#Ex.2
'''def media(*args):
    soma = sum(args)
    return f"Media: {(soma / len(args)):.1f}"

print(media(2, 4, 7, 9, 8, 5))'''


#Ex.3
'''def strings_separadas(*args):
    texto_junto = " ".join(args) # .join() junta tudo
    return f"Palavras: {texto_junto}"

print(strings_separadas("Python", "Java", "C#", "JavaScript"))'''


#Se usar "global" dentro de uma função ou algum local que declara a variavel local da para usar o mesmo nome e usando a global
# declarando ela como global, ai usa a global e nao substitui ela

#Ex.4 - Crie um programa que simule um banco, usando variaveis globais saldo e transações. Implemente as funções
#depositar(valor), sacar(valor) e extrato()
saldo = 0
transacoes = []

def escolher_opcoes():
    while True:
        print("1 - Depositar\n2 - Sacar\n3 - Extrato\n4 - Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            try:
                valor = float(input("Digite o valor do depósito: R$ "))
                depositar(valor)
            except ValueError:
                print("Digite apenas números.")

        elif escolha == "2":
            try:
                valor = float(input("Digite o valor do saque: R$ "))
                sacar(valor)
            except ValueError:
                print("Digite apenas números.")

        elif escolha == "3":
            extrato()

        elif escolha == "4":
            print("Obrigado por utilizar nosso banco!")
            break
        else:
            print("Opção Inválida...")


def depositar(valor):
    global saldo

    if valor > 0:
        saldo += valor
        print("Transação realizada com sucesso!")
        transacoes.append(f"Depósito: R$ + {valor:.2f}")
    else:
        print("O valor deve ser maior que 0!")


def sacar(valor):
    global saldo

    if valor <= 0:
        print("O saque deve ser maior que 0!")

    elif valor > saldo:
        print("Saldo insuficiente!")

    else:
        saldo -= valor
        print("Transação realizada com sucesso!")
        transacoes.append(f"Saque: R$ - {valor:.2f}")


def extrato():
    print("\n========== EXTRATO ===========")

    if len(transacoes) == 0:
        print("Não foram realizadas transações!")
    else:
        for transacao in transacoes:
            print(transacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n===============================")

escolher_opcoes()







