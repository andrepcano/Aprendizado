# Exercício 31

usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

if usuario == "admin":
    if senha == "1234":
        print("ACESSO TOTAL")
    else:
        print("Senha incorreta!")
else:
    print("Usuário incorreto!")

