'''
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.
'''
print('=='*20)
numero = int(input('Escolha um número: '))
print('=='*20)
for num in range(0, 11):
    print(f'{numero} x {num}= {numero*num}')
print('=='*20)