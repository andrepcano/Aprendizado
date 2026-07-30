# Exercício 36

dia_semana = input("Qual o dia da semana: ").lower()

if dia_semana == "sabado":
    print("Dia de festa!")

elif dia_semana == "domingo":
    condicao_fisica = input("Qual sua condição física: ")
    if condicao_fisica == "dores de cabeça":
        print("Recuperando, então precisa descansar!")
    else:
        print("Apenas descanse!")
else:
    print("Trabalho, trabalho, trabalho!!!")

