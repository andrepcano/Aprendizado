#Crie uma tupla preenchida com os 20 colocados da tabela do campeonato brasileiro, na ordem de colocação.
#Depois  mostre: A) apenas os 5 primeiros colocados, B)Os ultimos 4 colocados, C)Uma lista com os time em ordem de colocação
#D)Em que posição da tabela está o time da chapecoense

tabela_brasileirao = ("Palmeiras", "Flamengo", "Athletico Paranaense", "Fluminense", "RB Bragantino", "Bahia", "Botafogo", "Atlético-MG", "Corinthians", "Coritiba", "Cruzeiro", "São Paulo", "Vitória", "Santos", "Grêmio", "Internacional", "Vasco da Gama", "Remo", "Mirassol", "Chapecoense")

#A)
print(f"Os Cinco Primeiros Colocados: \n{tabela_brasileirao[:5]}\n")

#B)
print(f"Os Ultimos Quatro Colocados: \n{tabela_brasileirao[-4:]}\n")

#C)
for numero, time in enumerate(tabela_brasileirao, start=1):
    print(f"{numero} - {time}")

#D)
print(f"\nO time da Chapecoense esta em: {tabela_brasileirao.index("Chapecoense") + 1}")
