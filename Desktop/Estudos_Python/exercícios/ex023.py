'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
    Digite um número: 1834

    unidade: 4
    dezenas: 3
    centenas: 8
    milhar: 1
'''

numero = int(input('Digite um número entre 0 e 9999: '))

u = numero // 1%10
d = numero // 10%10
c = numero // 100%10
m = numero // 1000%10

print(f'O número {numero} possui:\n -> milhar: {m} \n -> centena: {c} \n -> dezena: {d} \n -> unidade: {u}')