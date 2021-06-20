'''
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

aluno_1 = str(input('Entre com o nome do 1º aluno: '))
aluno_2 = str(input('Entre com o nome do 2º aluno: '))
aluno_3 = str(input('Entre com o nome do 3º aluno: '))
aluno_4 = str(input('Entre com o nome do 4º aluno: '))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista_alunos)

print(f'A ordem sorteada foi: {lista_alunos}')