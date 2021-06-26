'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print(f'Escolha a Opção: \n  [1] {num} para binário: \n  [2] {num} para octal: \n  [3] {num} para hexadecimal: ')
opcao = int(input('Qual sua opção: '))

if opcao == 1:
    print(f'{num} em binário é {bin(num)[2:]}.')
elif opcao == 2:
    print(f'{num} em octal é {oct(num)[2:]}.')
elif opcao == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}.')
else:
    print('Opção INVÁLIDA.')