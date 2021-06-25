'''
Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
'''
from datetime import date 

ano_analisado = int(input('Digite o ano para analisar (caso seja ano atual digite 0): '))

if ano_analisado == 0:
    ano_analisado = date.today().year
if ano_analisado % 400 == 0 or ano_analisado % 4 == 0 and ano_analisado % 100 != 0:
    print(f'O ano de {ano_analisado} é BISSEXTO! ')
else:
    print(f'O ano {ano_analisado} não é BISSEXTO!')

