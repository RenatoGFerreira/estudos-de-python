'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

numero = randint(0, 5)
escolha = int(input('Digite um número de 0 a 5: '))
print(f'Pensei no {numero}')

print(f'Eu pensei no {numero} e você no {escolha}, portando você ', end='')

if numero == escolha:
    print('venceu!')
else:
    print('perdeu!')
