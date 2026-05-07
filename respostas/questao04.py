print('Contador de Dígitos')
numero = (int(input('Inteiro Positivo: ')))
while True:
    if numero > 0:
        break
    else:
        numero = int(input('Tem que ser postivo, brother. Digita de novo\n'))
    print('\n')

print(f'Número de Dígitos de {numero}: {len(str(numero))}')