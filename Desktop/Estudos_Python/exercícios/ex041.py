'''
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

    - Até 9 anos:   MIRIM
    - Até 14 anos:  INFANTIL
    - Até 19 anos:  JUNIOR
    - Até 20 anos:  SENIOR
    - Acima:        MASTER

'''

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Com {idade} anos: MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Com {idade} anos: INFANTIL')
elif idade > 15 and idade <= 19:
    print(f'Com {idade} anos: JUNIOR')
elif idade == 20:
    print(f'Com {idade} anos: SENIOR')
elif idade > 20:
    print(f'Com {idade} anos: MASTER')

