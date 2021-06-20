'''
    Faça um programa que leia a largura e a altura de uma parede em metos, calcule a sua àrea e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta, pinta uma área de 2m²
'''

largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))


area_total = largura * altura

print(f'Com a àrea da parede de {area_total}m² será necessário {area_total/2} litros de tinta.')

