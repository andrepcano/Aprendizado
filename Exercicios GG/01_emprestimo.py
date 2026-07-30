#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#O programa deve perguntar o salário, valor da casa, e quantas parcelas deseja pagar.
#O valor da prestação nao pode exceder de 30% do salário ou então o empréstimo será negado.

salario = float(input("Qual seu salário: "))
valor_casa = float(input("Qual o valor da casa que deseja comprar: "))
parcelas = float(input("Em quantas parcelas(meses) deseja pagar: "))

parcela_valor = valor_casa / parcelas
limite = (salario * 30) /100

if parcela_valor > limite:
    print("Emprestimo negado!!!")
elif parcela_valor < limite:
    print("Emprestimo aprovado!!!")
else:
    print("Emprestimo negado!!!")

print(f"o valor da prestação é de R$: {parcela_valor:.2f}")

