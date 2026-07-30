#Escreva um programa que leia um número inteiro qualquer.
#E peça para o usuário escolher qual será a base da conversão.
#-1 para bínario
#-2 para octal
#-3 para hexadecimal

numero = int(input("Digite um número e terá três opções de conversão: "))

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

   
opcoes(numero, opcao)

