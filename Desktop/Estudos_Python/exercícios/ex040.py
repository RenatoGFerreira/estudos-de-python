'''
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida.
    - Média abaixo de 5,0: REPROVADO
    - Média entre 5,0 e 6,9: RECUPERAÇÃO
    - Média 7,0 ou superior: APROVADO
'''

nota_1 = float(input('Nota 1 do aluno: '))
nota_2 = float(input('Nota 2 do aluno: '))

media = (nota_2 + nota_1) / 2

if media >= 7:
    print(f'media: {media:.2f} = APROVADO')
elif media < 5:
    print(f'media: {media:.2f} = REPROVADO')
else:
    print(f'media: {media:.2f} = RECUPERAÇÃO')