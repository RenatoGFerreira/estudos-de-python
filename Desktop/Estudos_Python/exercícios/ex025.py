'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
'''

nome_pessoa = str(input('Qual o nome completo da pessoa? ')).strip().lower().split()

sim_ou_nao = 'silva' in nome_pessoa

print(f'Tem "Silva" no nome? [True/False] {sim_ou_nao}')