# Exercício 11

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))

media = (nota_um + nota_dois + nota_tres) /3

if media >= 7.0:
    print(f"Sua média é de {media:.2f} e você esta APROVADO!!")
elif 5 <= media < 7.0:
    print(f"Sua média é de {media:.2f} e você esta de RECUPERAÇÃO!!")
else:
    print(f"Sua média é de {media:.2f} e você esta REPROVADO!!")

