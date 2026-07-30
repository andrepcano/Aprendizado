# Exercício 26

def saudaçao_personalizada(hora_dia):

    if hora_dia < 12:
        return "Bom Dia!!"
    elif 12 <= hora_dia < 18:
        return "Boa Tarde!!"
    else:
        return "Boa Noite!!"

hora_atual = float(input("Qual o horario atual(0-23): "))
print(saudaçao_personalizada(hora_atual))

