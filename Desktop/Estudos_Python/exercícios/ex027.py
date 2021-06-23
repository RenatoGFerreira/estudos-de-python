'''
Faça um programa que leia o nome completo de uma pessoa, mostando em seguida o primeiro e o ultimo nome separadamente.

Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''

nome = str(input('Digite o nome completo: ')).strip().split()

print(f'Primeiro Nome: {nome[0]} \nUltimo Nome: {nome[-1]}')
