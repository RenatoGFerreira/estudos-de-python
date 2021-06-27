'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''

for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont)
print('Fim do Programa.')


#OU DE FORMA FÁCIL TAMBÉM

for n in range(2, 51, 2):
    print(n)
print('Fim do Programa.')