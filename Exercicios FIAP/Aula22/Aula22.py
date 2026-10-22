#Abre o arquivo para leitura
'''arq = open("texto.txt", "r", encoding="utf-8")'''

#Lê todo o conteúdo do arquivo
'''conteudo = arq.read()
print(conteudo)'''

#Lê os primeiros 10 caracteres do arquivo
'''a = arq.read(10)
print(a)'''

#Lê linha por linha
'''linha = arq.readline()
print(linha)'''

#Lê todas as linhas em uma lista
'''linhas = arq.readlines()
print(linhas)'''

#Sobrescreve o início do arquivo
'''arq = open("texto.txt", "r+", encoding="utf-8")
arq.write("Olá, mundao!")'''

#Adiciona texto ao final do arquivo
'''arq = open("texto.txt", "a", encoding="utf-8")
arq.write("\nNova linha no final")'''

#Substitui todo o conteúdo do arquivo
'''arq = open("texto.txt", "w", encoding="utf-8")
arq.write("Texto novo")'''

#Cria um novo arquivo se ele não existir
'''arq = open("novo_texto.txt", "x", encoding="utf-8")
arq.write("Arquivo criado com sucesso")'''

#Fecha o arquivo depois de usar
'''arq.close()'''

#Explicação:
# open() abre o arquivo
# read() lê tudo
# read(10) lê 10 caracteres
# readline() lê uma linha
# readlines() lê todas as linhas em lista
# r+ permite ler e escrever
# a adiciona texto no final
# w sobrescreve tudo
# x cria um novo arquivo
# close() fecha o arquivo