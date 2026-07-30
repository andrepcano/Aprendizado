#Faça um programa que leia o ano de nascimento de um jovem.
#E informe, de acordo com sua idade.
#-Se ele ainda vai se alistar no exército.
#-Se é a hora de se alistar no exército.
#-Se já passou o tempo de se alsitar.
#O programa tambem devera mostrar o tempo restante

ano_nascimento = int(input("Qual seu ano de nascimento: "))
ano_atual = 2026
limite = 18
resultado_ano = ano_atual - ano_nascimento

if resultado_ano < limite:
    print("Ainda vai se alistar")
    tempo_restante = limite - resultado_ano
    print(f"Falta {tempo_restante} anos para se alistar!")
elif resultado_ano == limite:
    print("Está no ANO do alistamento não perca!!")
else: 
    print("VISH!!! Ja passou o tempo do alistamento!!")

