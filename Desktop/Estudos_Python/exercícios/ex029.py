'''
Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por km acima do limite
'''

velocidade = int(input('Velocidade do automóvel: '))

if velocidade <= 80:
    print(f'{velocidade} km/h, Velocidade Permitida.')
else:
    print(f'Acima do limite de velocidade, para {velocidade} km/h a multa é de R$ {(velocidade-80)*7},00')