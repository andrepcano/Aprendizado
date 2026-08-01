#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de 0 ate 20
#Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostralo por extenso

numeros_extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "desoito", "dezenove", "vinte")

try:
    escolha_numero = int(input("Escolha um número (entre 0 e 20) e ele aparecerá por extenso: "))
except ValueError:
    print("Digite um valor correto!")
    escolha_numero = int(input("Escolha um número (entre 0 e 20) e ele aparecerá por extenso: "))

while escolha_numero not in range(21):
    print("Tente novamente...")
    escolha_numero = int(input("Escolha um número (entre 0 e 20) e ele aparecerá por extenso: "))

print(numeros_extenso[escolha_numero])
