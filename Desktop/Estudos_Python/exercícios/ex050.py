'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar, desconsidere-o.
'''

soma = 0

for cont in range(0, 6):
    numero = int(input(f'Digite o {cont+1}º número: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma total é {soma}.')