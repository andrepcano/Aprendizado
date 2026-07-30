# -Ex.1 Solicite para o usuário o salario 
# e retorne o respectivo desconto e valor a ser recebido em funçao da tabela de descontos do Brasil
#
# Salário de Contribuição (R$) 	Alíquota progressiva para fins de recolhimento ao INSS
# Até R$ 1.621,00	7,5%
# De R$ 1.621,01 a R$ 2.902,84	9%
# De R$ 2.902,85 até R$ 4.354,27	12%
# De R$ 4.354,28 até R$ 8.475,55	 14%

salario = float(input("Digite o seu salário: "))
if salario <= 1621.00:
    desconto = (salario * 7.5) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
elif 1621.01 <= salario <= 2902.84:
    desconto = (salario * 9) /100
    print(f"O desconto do INSS é de R$: {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
elif 2902.85 <= salario <= 4354.27:
    desconto = (salario * 12) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")
else:
    desconto = (salario * 14) /100
    print(f"O desconto do INSS é de R$ {desconto:.2f}")
    print(f"O valor a ser recebido é de R$ {salario - desconto:.2f}")

