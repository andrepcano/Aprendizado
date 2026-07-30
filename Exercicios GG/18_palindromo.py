#Crie um programa que leia uma frase qualquer e diga se ela é
#um palindromo, desconsiderando os espaços

#DIFICIL DEMAIS

texto = input("Escreva algo e direi se é um palíndromo: ")
texto_minusculo = texto.lower()
texto_junto = ""
texto_invertido = ""

for c in texto_minusculo:
    if c != " ":
        texto_junto = texto_junto + c

for c in texto_junto:
    texto_invertido = c + texto_invertido
if texto_junto == texto_invertido:
    print("O texto {} é um palíndromo".format(texto))
else:
    print("O texto {} não é um palíndromo".format(texto))

