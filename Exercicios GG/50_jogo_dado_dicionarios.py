#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
#Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo
#que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter

#Criando jogadores
jogadores = {
    "jogador_1": randint(1,6),
    "jogador_2": randint(1,6),
    "jogador_3": randint(1,6),
    "jogador_4": randint(1,6),
}

ranking = dict()
for keys, values in jogadores.items():      # items = keys and values
    print(f"O {keys} tirou {values} no dado!")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("-"*30)
for i, v in enumerate(ranking):
    print(f"{i + 1} lugar: {v[0]} com {v[1]}") 
    sleep(1)






