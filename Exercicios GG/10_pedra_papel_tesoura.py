#PEDRA, PAPEL OU TESOURA

import random

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
    print("Opçao Invalida")

