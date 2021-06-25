'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
num_1 = int(input('Digite o número 1: '))
num_2 = int(input('Digite o número 2: '))
num_3 = int(input('Digite o número 3: '))

maior = num_1
menor = num_1

if num_2 > maior:
    maior = num_2
else:
    menor = num_2
if num_3 > maior:
    maior = num_3
if num_3 < menor:
    menor = num_3

print(f'O maior é {maior} e o menor {menor}.')