'''
Faça um programa que leia uma frase pelo teclado e mostre:

*Quantas vezes aparece a letra "A"
*Em que posição ela aparece a primeira vez.
*Em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip().lower()

total_a = frase.count('a')
primeira_a = frase.find('a')
ultima_a = frase.rfind('a')

print(f'Ao todo na frase: {frase} \n temos um total de {total_a} letras "A" \n sendo a primeira na posição {primeira_a} \n e a última está na posição {ultima_a}.')