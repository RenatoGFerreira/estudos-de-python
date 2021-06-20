'''
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

import math

cateto_oposto = float(input('Entre com o comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Entre com o comprimento do Cateto Adjacente: '))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f'Para o cateto oposto de {cateto_oposto} e cateto adjacente de {cateto_adjacente} temos o comprimento da hipotenusa de {hipotenusa:.2f}')