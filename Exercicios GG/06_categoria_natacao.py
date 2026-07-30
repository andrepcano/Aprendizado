#A confederação nacional de natação precisa de um programa que leia o ano
#de nascimento de um atleta e mostre sua categoria conforme a idade:
#ate 9 anos: mirim
#ate 14 anos: infantil
#ata 19 anos: juniot
#ate 20 anos> sênior
#acima: mastes

idade = int(input("Qual a sua idade e direi qual categoria es: "))

if idade <= 9:
    print(f"Categoria mirim {idade}")
elif idade > 9 and idade <= 14:
    print(f"Categoria infantil {idade}")
elif idade > 14 and idade <= 19:
    print(f"Categoria junior {idade}")
elif idade > 19 and idade == 20:
    print(f"Categoria sênior {idade}")
else:
    print(f"Você é da categoria MASTER e tem {idade} anos")

