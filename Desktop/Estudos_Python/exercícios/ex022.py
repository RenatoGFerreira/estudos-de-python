'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas
* O nome com todas as letras minúsculas
* Quantas letras ao todo (sem considerar espaços)
* Quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome: ')).strip()

print(f'Seu nome é {nome}.')
print(f'Seu nome em maiúsculo fica {nome.upper()}.')
print(f'Seu nome em minúsculo fica {nome.lower()}.')
name_nospace = len(nome) - nome.count(' ')
print(f'Seu nome possui {name_nospace} letras')
print(f'Seu primeiro nome é {nome.split()[0]}')