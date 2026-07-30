# -Ex.2 Crie um algoritmo para solicitar o salario recebido durante o mes
#  e calcule o imposto a ser pago, bem como o salario a receber
#
#  salario = input for user
#  imposto = 15%

salario = float(input("Digite seu salario: "))
imposto = (salario * 15) /100

print(f"O imposto a ser descontado do seu salario é de R$ {imposto:.2f}")
print(f"O valor a ser recebido ja com o imposto descontado é de R$ {salario - imposto:.2f}")

