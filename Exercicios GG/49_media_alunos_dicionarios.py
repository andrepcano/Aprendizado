#Faça um programa que leia nome e media de um aluno, guardando tambem a situação em um dicionario.
#No final, mostre o conteudo da estrutura na tela.

alunos = dict()
alunos["nome"] = str(input("Nome: "))
alunos["media"] = float(input(f"Media de {alunos["nome"]}: "))

if alunos["media"] >= 7:
    alunos["situacao"] = "Aprovado"
elif 5 <= alunos["media"] <7:
    alunos["situacao"] = "Recuperação"
else:
    alunos["situacao"] = "Reprovado"

print(alunos)






