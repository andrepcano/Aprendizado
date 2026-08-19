import utils

palavra = input("Digite uma palavra: ")
print(f"Quantidade de vogais na palavra {palavra}: {utils.cont_vogais(palavra)}")
print(f"Palavra invertida: {utils.reverter_string(palavra)}")
print(f"Espaços entre as palavras: {utils.conta_espacos(palavra + " Casa")}")