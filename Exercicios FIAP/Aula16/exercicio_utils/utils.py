def cont_vogais(string):
    vogais = 0

    for i in string:
        if i in "aeiou":  
            vogais += 1

    return vogais


def reverter_string(string):
    palavra_invertida = ""

    for letra in string:
        palavra_invertida = letra + palavra_invertida

    return palavra_invertida


def conta_espacos(string):
    cont = 0

    for i in string:
        if i == " ":
            cont += 1

    return cont
            
