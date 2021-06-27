'''
Crie um programa que faça o computador jogar JOKENPÔ com você.
'''
from time import sleep
from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
print('{:=^40}'.format(' Lets Play Jo-Ken-Pô!!! '))
print('Escolha uma opção: \n [1] Pedra\n [2] Papel\n [3] Tesoura')

opcao = int(input('Opção: '))
opcao_computador = randint(0,2)

print('=='*20)
print('    JO')
sleep(1)
print('       KEN')
sleep(1)
print('    PÔ')
print('=='*20)
print(f'Computador jogou {itens[opcao_computador]} e você jogou {itens[opcao-1]}.')

if opcao_computador == 0:               #PEDRA
    if opcao == 1:
        print('Empataram!')
    elif opcao == 2:
        print('Jogador Ganhou!')
    elif opcao == 3:
        print('Computador Venceu!')

elif opcao_computador == 1:             #PAPEL
    if opcao == 1:
        print('Computador Venceu!')
    elif opcao == 2:
        print('Empataram!')
    elif opcao == 3:
        print('Jogador Ganhou!')

elif opcao_computador == 2:             #TESOURA
    if opcao == 1:
        print('Jogador Ganhou!')
    elif opcao == 2:
        print('computador Venceu!')
    elif opcao == 3:
        print('Empataram!')
print('=='*20)
