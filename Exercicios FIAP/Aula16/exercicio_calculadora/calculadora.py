#Ex.1 - Crie um programa chamado calculadora.py que chama dois módulos, um contendo as funções de soma
#e subtração e o outro contendo as de multiplicação e divisão.
import contas_basicas, contas_divisao_multiplicacao

print(contas_basicas.soma(10, 5, 8))
print(contas_basicas.subtracao(10, 5, 8))

print(contas_divisao_multiplicacao.multiplicacao(10, 5, 8))
print(contas_divisao_multiplicacao.divisao(10, 5, 8))





