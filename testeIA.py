""" Primeiro programa usando IA (codex)

while True:
    try:
        numero = float(input("Digite um número (negativo para sair): ").replace(",", "."))
    except ValueError:
        print("Digite um número válido.")
        continue

    if numero < 0:
        break

    for i in range(1, 11):
        print(f"{numero:g} x {i} = {numero * i:g}")"""
