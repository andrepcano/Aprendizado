# DICIONARIOS

# TIPOS QUE PODEM NO DICIONARIO
'''d = {
    : 1.85,
    'long'lat'': 20.45,
    10: 'teste',
    1.45: [[0, 1], [2, 3]]
}
print(d[10])'''# ACESSO PELA CHAVE

#Ex.1 - Escreva um programa que dada a lista a seguir:

'''dados = [
    {"dia": 12, "mes": 2,"ano": 2019, "temp": 30.5},
    {"dia": 18, "mes": 3, "ano": 2019, "temp": 29.1},
    {"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
    {"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
]
# Imprima a resposta como (DEIXE BONITO)

respec_dados = {}

for dado in dados:
    data = f"{dado["dia"]:02d}/{dado["mes"]:02d}/{dado["ano"]}"
    respec_dados[data] = dado["temp"]

print("=----- TEMPERATURAS REGISTRADAS -----=")

for data, temperatura in respec_dados.items(): #.items() pega apenas os items do dicionario
    print(f"Data: {data} | Temperatura: {temperatura:.1f}°C")'''


#Ex.2 - Crie um dicionario com tres pares chave-valor. As chaves devem ser os nomes de tres frutas e,
#os valores suas respectivas cores

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}'''


#Ex.3 - Usando o dict criaco no Ex anterior, acesse e imprima a cor de uma adas frutas

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}

print(f"{frutas["morango"]}")'''


#Ex.4 - Adicione  um novo par chave-valor ao dicionario, representando outra fruta e sua cor.

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}

frutas["maça"] = "Vermelho"

print(frutas)'''


#Ex.5 - Remove uma fruta do dicionario utilizando o metodo .pop()

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}

frutas.pop("abacate")
print(frutas)'''


#Ex.6 - Itere sobre o dicionario e imprima apenas as chaves (nomes das frutas)

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}

print(frutas.keys())'''



#Ex.7 - Itere sobre o dicionario e imprima apenas os valores (cor das frutas)

'''frutas = {
    "banana": "Amarela",
    "morango": "Vermelho",
    "abacate": "Verde"
}

print(frutas.values())'''


#Ex.8 - Verifique se a fruta banana esta presente no dicionario e imprima uma mensagem com base no resultado

'''frutas = {
    "morango": "Vermelho",
    "banana": "Amarela",
    "abacate": "Verde"
}

encontrou = False

for nome, cor in frutas.items():
    if nome == "banana":
        encontrou = True
        break

if encontrou == True:
    print("TEM banana no dicionario!")
else:
    print("NÃO banana no dicionario!")'''



#Contrua um dicionario de cadastro de pessoas, Pegue o usuario e a quantidade de pessoas, cadastre como
#chave o nome e como valor uma lista com idade e altura

'''cadastro_pessoas = {}

qntd = int(input("Quantas pessoas quer cadastrar: "))

for i in range(qntd):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    cadastro_pessoas[nome] = [idade, altura]

print("\n=----- PESSOAS CADASTRADAS -----=\n")

for nome, dados in cadastro_pessoas.items():
    idade, altura = dados
    print(f"Nome: {nome}: Idade: {idade}, Altura: {altura}")'''


#(zip) serve para juntar duas listas e transformar a primeira em chaves e a segunda em valores










