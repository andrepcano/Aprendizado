#Elabore um programa que calcule o valor a ser pago por
#um produto, considerando o seu preço normal + condição de pagamento
#A vista dinheiro/cheque: 10% de desconto
#A vsitra cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no crtão: 20% de juros

produto = input("Qual o nome do produto: ")
preco_normal = float(input("Digite o preço normal do produto: "))
condicao_pagamento = int(input("Condição de Pagamento: \n" \
                                "1- A vista dinheiro/cheque\n" \
                                "2- A vista cartão\n" \
                                "3- Em ate 2x no cartão\n" \
                                "4- Em 3x ou mais.\n"))

avista_cartao = (preco_normal *5) / 100
avista_normal = (preco_normal * 10) / 100
duas_vezes = preco_normal
tres_vezes_mais = preco_normal / 20  

resultado_avista_cartao = preco_normal - avista_cartao
resultado_avista_normal = preco_normal - avista_normal
resultado_tres_vezes = preco_normal + tres_vezes_mais

if condicao_pagamento == 1:
    print(f"O preço do desconto é {avista_normal}")
    print(f"O preço com desconto é {resultado_avista_normal}")
elif condicao_pagamento == 2:
    print(f"O preço do desconto é {avista_cartao}")
    print(f"O preço com desconto é {resultado_avista_cartao}")
elif condicao_pagamento == 3:
    print(f"O preço é o mesmo")
else:
    print(f"O preço do juros é {tres_vezes_mais}")
    print(f"O preço ja com juros é {resultado_tres_vezes}")

