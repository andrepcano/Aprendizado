#Exercicios (IF, ELIF, ELSE)

#Escreva um rpograma que faça o computador escolher entre 1 e 5
# e peça para o usuário tentar descobrir qual numero foi
#o programa deve mostrar se o usuário venceu ou perdeu

import random

tentativa = int(input("Tente acertar o número escolhido entre 0 a 5: "))

numero = random.randint(0, 6)

if tentativa == numero:
    print("VOCÊ ACERTOU!")
else:
    print("Você ERROU")

