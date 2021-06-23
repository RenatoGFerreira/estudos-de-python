'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''

cidade = str(input('Nome da cidade: ')).strip().lower()

sim_ou_não = 'santo' in cidade[0:5]

print(f'O nome da cidade começa com Santo? [True/False] {sim_ou_não}')

