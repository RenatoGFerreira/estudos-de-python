#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Preço do Produto: '))

new_price = price * 0.95

print(f'O produto de R${price:.2f} com o desconto de 5% fica R${new_price:.2f}. ')