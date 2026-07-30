# -Ex.3 Solicite o salario do usuario é descubra o quanto de aumento teve

salario_antigo = float(input("Qual era seu salário: "))
aumento = float(input("Quantos porcento de aumento você teve: "))

salario_atual = (salario_antigo * aumento) /100
print(f"O valor do aumento no seu salário é deR$: {salario_atual:.2f}")
print(f"O valor total do seu salário atual é de R$ {salario_antigo + salario_atual:.2f}")

