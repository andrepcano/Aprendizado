# Exercício 35

valor = float(input("Digite um valor: "))
pessoa = input("Você é VIP (Sim) ou (Não): ").lower()

if valor >= 1000:
    if pessoa == "sim":
        desconto_vip = valor /20
        valor_desconto_vip = valor - desconto_vip
        print("Você te direito a 20% de desconto, o desconto fica de {}R$ e o valor final é {}R$".format(desconto_vip, valor_desconto_vip))
else:
    desconto_sem_vip = valor / 10
    valor_desconto = valor - desconto_sem_vip
    print("Você tem direito a 10% de desconto, o desconto fica de {}R$ e o valor final é {}R$".format(desconto_sem_vip, valor_desconto))

