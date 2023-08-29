'''
2. Crie um programa que leia uma velocidade de um carro e multe se
passar com velocidade maior que 80km/h. mostre que ele foi multado.
a multa é de 7 R$ por cada km acima do limite.
'''

velocidade = input("Digite a velocidade do veículo: ")

velocidade_int = 0
limite_velocidade = 80

try:
    velocidade_int = int(velocidade)
except ValueError:
    raise ValueError("Digite uma velocidade válida!")

if velocidade_int > limite_velocidade:
    valor_multa = (velocidade_int - limite_velocidade) * 7.0
    print(f"Você foi multado por excesso de velocidade, o valor da multa é: R${valor_multa}")
else: 
    print("Velocidade dentro do limite!")

