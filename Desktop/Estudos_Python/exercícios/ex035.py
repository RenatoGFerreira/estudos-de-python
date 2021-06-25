'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
print('-='*20)
print('Analisador de Triângulo')
print('-='*20)

reta_1 = float(input('Reta 1:'))
reta_2 = float(input('Reta 2:'))
reta_3 = float(input('Reta 3:'))

if reta_1 <= (reta_2 + reta_3):
    if reta_2 <= (reta_1 + reta_3):
        if reta_3 <= (reta_1 + reta_2):
            print('Formam um triângulo.')
else:
    print('Não formam um triângulo.')
