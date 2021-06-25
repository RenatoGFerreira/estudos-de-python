'''
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou entâo o empréstimo será
negado.
'''

valor_casa = float(input('Qual o valor da casa? R$ '))
salario_comprador = float(input('Qual o seu salário? R$ '))
anos_pagar = float(input('Quantos anos a pagar? '))

margem_aprovada = salario_comprador * 0.3
parcela_aprovada = valor_casa / anos_pagar / 12
parcelas = anos_pagar * 12

if margem_aprovada >= parcela_aprovada:
    print(f'CONDIÇÃO APROVADA! \nSerão {parcelas:.0f} parcelas de R${parcela_aprovada:.2f}')
else:
    print(f'NÃO APROVADA! \n Para condições de aprovamento é necessário que: \n -> A casa tenha o preço limite de até R${(margem_aprovada * anos_pagar * 12):.2f}. \n -> Ou o prazo total deverá aumentar para {(valor_casa / margem_aprovada):.0f} meses. \n -> Ou a condição do comprador deverá ser superior a R${(parcela_aprovada * 3.34):.2f}.')