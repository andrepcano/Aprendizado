#Faça um programa que jogue par ou impar com o computador, o jogo so sera interrompido quando o jogador perder
# mostrando o total de vitorias consecutivas.

import random

quantidade_vitorias = 0

while True:
    numero_aleatorio = random.randint(1, 10)
    escolha_user = input("Digite par ou impar: ").strip.lower()
    
    try:
      numero_user = int(input("Digite um número entre 1 e 10: "))
    except ValueError:
      print("Digite apenas números.")
      continue

    if numero_user not in range(1, 11):
        print("Digite o número entre 1 e 10")
        continue

    soma = numero_aleatorio + numero_user
    
    if escolha_user not in ("par", "impar"):
        print("Digite apenas par ou impar.")
        continue

    if soma % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
        
    print(f"A soma dos números é {soma}, que é {resultado}")

    if escolha_user == resultado:
            print(f"Parabens, você ganhou escolhendo {escolha_user}")
            quantidade_vitorias += 1
    else:
        print(f"Você perdeu, ganhando {quantidade_vitorias} consecutivas!")
        break

