# Exercício 37

valor_um = float(input("Digite um valor: "))
valor_dois = float(input("Digite um valor: "))
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
    print("Escolha Inválida!")

