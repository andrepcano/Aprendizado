# Exercício 8

peso = float(input("Digite seu peso atual em (Kg): "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura **2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.2f} e você está abaixo do peso!!")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de {imc:.2f} e você está com o peso normal!!")
else:
    print(f"Seu IMC é de {imc:.2f} e você está ACIMA do peso!!")

