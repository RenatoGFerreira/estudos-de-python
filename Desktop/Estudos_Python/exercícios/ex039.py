'''
Faça um program que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - Se ele ainda vai se alistar ao serviço militar.
    - Se é a hora de se alistar.
    - Se já passou do tempo do alistamento.

Seu programa tambem deverá mostrar o tempo que falta ou passou do prazo.
'''

from datetime import date

ano_atual = date.today().year
print(ano_atual)

ano_nascimento = int(input('Qual o seu ano de nascimento? '))
if ano_atual - ano_nascimento < 18:
    print(f'Faltam {18 - (ano_atual - ano_nascimento)} anos para o seu alistamento.')
elif ano_atual - ano_nascimento > 18:
    print(f'Já se passaram {(ano_atual - ano_nascimento) - 18} anos do seu alistamento.')
else:
    print('Com 18 anos está no ano de alistamento.')

