'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
PAGAMENTO:
    - à vista DINHEIRO/CHEQUE: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2X no cartão: preço normal
    - 3X ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS PREÇOBOM '))
preco_produto = float(input('\nDiga o valor do produto: R$'))
print('\n[1] à vista DINHEIRO/CHEQUE: 10% de desconto \n[2] à vista no cartão: 5% de desconto \n[3] em até 2X no cartão: preço normal \n[4] 3X ou mais no cartão: 20% de juros\n')
forma_pagamento = int(input('Qual a forma de pagamento? '))

if forma_pagamento == 1:
    print(f'R${preco_produto:.2f} a vista reajustado com 10% de desconto = R${(preco_produto*0.9):.2f}.')
elif forma_pagamento == 2:
    print(f'R${preco_produto:.2f} a vista cartão reajustado a 5% de desconto = R${(preco_produto*0.95):.2f}.')
elif forma_pagamento == 3:
    print(f'R${preco_produto:.2f} parcelado a duas vezes de R${(preco_produto / 2):.2f}.')
elif forma_pagamento == 4:
    print(f'R${preco_produto:.2f} parcelado em 3x no cartão com juros de 20% a parcela fica 3 x R${((preco_produto * 1.2) / 3):.2f}')
else:
    print(f'Opção {forma_pagamento} sai da operação.')