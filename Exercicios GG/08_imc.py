#Desenvolva um logica que leia o peso e a altura de uma pessoa,
#calcule seu IMC e mostre seu resultado, de acordo com a tabela
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso Ideal
#Entre 25 a 30: Sobrepeso
#Entre 30 ate 40: Obesidade
#Acima de 40: Obesidade Mórbida

altura = float(input("Qual a sua altura em (M): "))
peso = float(input("Qual seu pesoem (Kg): "))
imc = peso / altura**2

if imc < 18.5:
    print(f"Seu IMC é {imc} e você está ABAIXO do peso")
elif 18.5 < imc < 25:
    print(f"Seu IMC é {imc} e você está com o peso IDEAL")
elif 25 < imc < 30:
    print(f"Seu IMC é {imc} e você esta com SOBREPESO")
elif 30 < imc < 40:
    print(f"Seu IMC é {imc} e você está com OBESIDADE")
else:
    print(f"Seu IMC é {imc} e esta com OBESIDADE MÓRBIDA")

