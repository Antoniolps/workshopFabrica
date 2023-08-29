'''
1. Crie um programa que receba uma idade e retorne se pode obter 
carteira de motorista(CNH)
'''

idade = input('Digite sua idade: ')

idade_em_int = 0

try:
    idade_em_int = int(idade)
except ValueError:
    raise ValueError("Digite uma idade válida!!")

if idade_em_int >= 18:
    print('Você está apto a tirar a carteira.')
else:
    print('Seu momento ainda não chegou.')