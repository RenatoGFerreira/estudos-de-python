'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. calcule o preço da passagem:
    Viagem até 200km R$0,50 por km
    Viagem acima de 200km R$0,45 por km
'''

viagem = int(input('Qual a distância em Km da viagem? '))

if viagem <= 200:
    preco = viagem * 0.5
else:
    preco = viagem *0.45

print(f'O preco da passagem ficará em R${preco:.2f}.')
