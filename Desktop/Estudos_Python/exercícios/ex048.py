'''
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.
'''

soma = 0
contador = 0

for cont in range(1, 500):
    if cont % 3 == 0:
        if cont % 2 == 1:
            contador += 1
            soma +=cont
print(f'A soma de todos os {contador} numeros somados é igual a {soma}.')