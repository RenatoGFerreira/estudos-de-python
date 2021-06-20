#Faça um algoitmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Salário total: R$'))
salary_adjust = salary * 1.15

print(f'Para o salário de R${salary:.2f}, o salário com o aumento de 15% passa a ser: R${salary_adjust:.2f}.')