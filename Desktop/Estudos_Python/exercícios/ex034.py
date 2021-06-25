'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

    Para salários superiores a R$1.200,00, calcule um aumento de 10%
    Para os inferiores ou iguais a R$1200,00, o aumento e de 15%
'''

salario = float(input('Diga o salário: '))

if salario >= 1200:
    salario_ajuste = salario * 1.1
else:
    salario_ajuste = salario * 1.15

print(f'O salário de R${salario:.2f} com o aumento e ficará com R${salario_ajuste:.2f} ')