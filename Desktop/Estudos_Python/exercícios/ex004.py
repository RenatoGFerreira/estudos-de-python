'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informaçoes possíveis sobre ele.'''

algo = input('Digite algo: ')

print('É número: ', algo.isnumeric())
print('Está em maiúsculo: ', algo.isupper())
print('É letra: ', algo.isalpha())
print('Está em minusculo: ', algo.islower())
print('Está captalizada: ', algo.istitle())