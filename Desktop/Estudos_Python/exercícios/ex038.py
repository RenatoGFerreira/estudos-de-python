'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    -O primeiro valor é maior.
    -O segundo valor é maior.
    -Não existe valor maior, os dois são iguais
'''

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero_1 > numero_2:
    print('O primeiro número é maior que o segundo.')
elif numero_1 < numero_2:
    print('O segundo número é maior que o primeiro.')
else:
    print('Não existe valor maior, os dois são iguais.')
