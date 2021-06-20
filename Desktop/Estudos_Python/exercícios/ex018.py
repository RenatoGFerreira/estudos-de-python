'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Para o ângulo de {angulo:.1f}º, \n -> Seno: {seno:.2f} \n -> Cosseno: {cosseno:.2f} \n -> Tangente: {tangente:.2f}')

