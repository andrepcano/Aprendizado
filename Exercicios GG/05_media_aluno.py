#Crie um programa que leia duas notas 
#de um aluno e calcule sua média, mostrando uma mensagem no final.
#de acordo com a média atingida.

nota_1 = float(input("Digite sua nota 1: "))
nota_2 = float(input("Digite sua nota 2: "))
nota_3 = float(input("Digite sua nota 3: "))
media = (nota_1 + nota_2 + nota_3) / 3

if media < 5.0:
    print(f"A sua média foi de {media:.2f} e você está REPROVADO!")
elif media >= 5 and media <= 6.9:
    print(f"A sua média foi de {media:.2f} e você está de RECUPERAÇÃO!")
else:
    print(f"Sua nota foi de {media:.2f} e você está APROVADO!!")

