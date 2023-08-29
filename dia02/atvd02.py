'''
1. Crie um programa que peça um numero e mostre o 
seu sucessor e antecessor
'''
num = input('Digite um numero: ')

antecessor = 0 
sucessor = 0

try:
    sucessor = int(num) + 1
    antecessor = int(num) - 1
except ValueError:
    raise ValueError("Digite um numero válido!")
    
print(f"O numero digitado foi {num}, seu sucessor é {sucessor} e seu antecessor {antecessor}")


# Mostrando o tipo da variável
print(type(num))



