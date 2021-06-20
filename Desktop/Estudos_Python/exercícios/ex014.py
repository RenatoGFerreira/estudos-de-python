#Escreva um programa que converta uma temperatura digitada em ºC E CONVERTA PARA ºF.


temperature_celsius = float(input('Enter with temperature Celsius: '))
temperature_fahrenheit = ((9* temperature_celsius)/5)+32

print(f'A temperatura {temperature_celsius}ºC é o mesmo que {temperature_fahrenheit}ºF.')
