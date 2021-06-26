'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

    - EQUILÁTERO: todos os lados iguais
    - ISOSCELES: dois lados iguais
    - ESCALENO: todos os lados diferentes
'''

lado_1 = float(input('1º lado do triângulo: '))
lado_2 = float(input('2º lado do triângulo: '))
lado_3 = float(input('3º lado do triângulo: '))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
    if lado_1 != lado_2 != lado_3:
        print('Triângulo ESCALENO.')
    elif lado_1 == lado_2 == lado_3:
        print('Triângulo EQUILÁTERO.')
    else:
        print('Triângulo ISOCELES.')
else:
    print('Um triângulo não pode ser formado quando um lado é igual ou maior que a soma dos outros dois lados.')

