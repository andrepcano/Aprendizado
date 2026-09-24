#BUBBLE SORT
'''lista = [45, 12, 87, 98, 22, 31]

                                       # len(lista) - 1 == 5                 
for j in range(len(lista) - 1, 0, -1): # range(5, 0, -1) => [5,4,3,2,1] É como se fosse essa lista
    for i in range(j):                 # Início, limite, passo 
        if (lista[i] > lista[i + 1]):
            numero_maior = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = numero_maior

print(lista)
'''


#SELECTION SORT
#Crie uma função que retorne o índice do menor elemento de uma lista, a partir de uma posição inicial dada.

'''lista = [12, 68, 95, 41, 10, 71]

def indice_menor(lista, inicio):
    indice_menor = inicio

    for i in range(inicio + 1, len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i

    return indice_menor

new_menor = indice_menor(lista, 0)

aux = lista[new_menor]
lista[new_menor] = lista[0]
lista[0] = aux
print(lista)'''



#INSERTION SORT = Ele pega uma lista que está inicialmente desordenada e vai construindo uma parte ordenada,
#colocando cada novo elemento na posição correta.

#Crie uma função que, dado uma lista e um indice i, insere o elemento de índice i entre os elementos
#das posições 0 e i-1 (pré-ordenados), de forma que todos elementos continuem ordenados

lista = [10, 9, 8, 15]

for i in range(1, len(lista)): # começa no 1 por que consideramos que o elemento 0 JA esta ordenado
    num_guardado = lista[i]
    j = i - 1 # num que vai ser comparado com o num_guardado
    while j >= 0 and lista[j] > num_guardado:
        lista[j + 1] = lista[j]
        j -= 1

    lista[j + 1] = num_guardado

print(lista)













