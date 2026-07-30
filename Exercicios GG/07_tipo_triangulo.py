#Desafio triângulos, acrescentando o recurso de mostrar que tipo de 
#triãngulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

seg_um = float(input("Digite o tamanho do segmento 1: "))
seg_dois = float(input("Digite o tamanho do segmento 2: "))
seg_tres = float(input("Digite o tamanho do segmento 3: "))


if seg_um < seg_tres + seg_dois or seg_dois < seg_tres + seg_um or seg_tres < seg_dois + seg_um:
    print("Pode formar um triângulo ", end='')
    if seg_um == seg_tres and seg_tres == seg_dois:
        print("EQUILÁTERO")
    if seg_tres == seg_dois != seg_um or seg_um == seg_dois != seg_tres or seg_tres == seg_um != seg_dois :
        print("ISÓSCELES")
    if seg_dois != seg_tres != seg_um:
        print("ESCALENO")
else: 
    print("Não da para formar um triângulo")

