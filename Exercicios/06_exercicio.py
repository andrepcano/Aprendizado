# Exercício 6

atividade_a = int(input("Digite o tempo gasto na atividade A: "))
atividade_b = int(input("Digite o tempo gasto na atividade B: "))
atividade_c = int(input("Digite o tempo gasto na atividade C: "))

if atividade_a + atividade_b + atividade_c > 0:
    print(f"O tempo total gasto nas atividades é de {atividade_a + atividade_b + atividade_c} dias!!")
else:
    print("ERRO!! os dias nao podem ser negativos!!")

