'''
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
#nome deles e escrevendo o nome do escolhido.
'''

from random import choice, randint

aluno_1 = str(input('Digite o nome do 1º aluno: '))
aluno_2 = str(input('Digite o nome do 2º aluno: '))
aluno_3 = str(input('Digite o nome do 3º aluno: '))
aluno_4 = str(input('Digite o nome do 4º aluno: '))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

sorteado = choice(lista_alunos)
print(sorteado)