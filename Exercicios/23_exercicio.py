# Exercício 23

while True:
    nome_user = input("Digite seu nome de usuário: ")
    senha_user = input("Digite sua senha: ")

    if len(nome_user) < 5:
        print("O nome de usuário deve conter pelo menos 5 caractéres!!")
        continue
    elif len(senha_user) < 8:
        print("A senha deve conter pelo menos 8 caractéres!!")
        continue
    print("Cadastro realizado com Sucesso!!")
    break;

