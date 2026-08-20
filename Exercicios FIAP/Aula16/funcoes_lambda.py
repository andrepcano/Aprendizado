#def soma(a, b):  (forma usando FUNÇÃO)
#   return a + b

#soma = lambda a, b: a + b #usando LAMBDA
#res = soma(1, 2)
#print(res)

#Ex.1 Crie uma função lambda que retorne a soma de 3 numeros

'''soma = lambda a, b, c: a + b + c
res = soma(1, 2, 3)
print(res)'''

#Ex.2 Crie uma função lambda para inverter uma string

'''inverter_string = lambda string: string[::-1]
res = inverter_string("String")
print(res)'''

#Ex.3 Crie uma função lambda que verifica se a String é um palíndromo

'''eh_palindromo = lambda string: string == string[::-1]
palavra = str(input("Digite uma palavra: "))

if eh_palindromo(palavra) == True:
    print("É um palindromo!")
else:
    print("Não é um palíndromo!")'''


#l2 = [ expressao for item in iteravel ]

'''def qualquer(a):
    return (a + 10) / 2.5

l2 = [qualquer(i) for i in range(10) if i % 2 == 0] # dando ".append" direto 
print(l2)'''

#Ex.4 Crie uma lista com os quadrados dos numeros de 1 a 10

'''lista_quadrados = [i**2 for i in range(10)]
print(lista_quadrados)'''


#Ex.5 Gere uma lista contendo apenas os numeros pares de 1 a 20

'''lista_pares = [ i for i in range(20) if i % 2 == 0]
print(lista_pares)'''


#Ex.6 Crie uma lista contendo o comprimento de cada palavra na lista
# ["Python", "List", "Comprehension", "Exercicios"]


