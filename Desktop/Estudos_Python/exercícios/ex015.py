'''
    Escreva um programa que pergunte a quantidade de Km percorrido por um carro aluagado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
'''

dias_alugado = float(input('Dias alugados: '))
km_rodado = float(input('Quilômetros rodados: '))

preco_total = dias_alugado * 60 + km_rodado * 0.15

print(f'O valor total a pagar é de R${preco_total:.2f}')
