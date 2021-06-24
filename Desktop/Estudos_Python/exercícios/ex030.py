'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''

impar_ou_par = int(input('Número: '))

if impar_ou_par % 2 == 1:
    print('Impar')
else:
    print('Par')