from math import sqrt

print('Seu Número É Perfeito?')
numero = int(input('Inteiro Positivo: '))
while True:
    if numero > 0:
        break
    else:
        numero = int(input('Tem que ser positivo, pô!\nInteiro Positivo: '))
        print('\n')
lilBludMaioria = 0
hãâ = 1

while hãâ <= int(sqrt(numero)):

    if numero % hãâ == 0:
        if hãâ != numero:
            lilBludMaioria += hãâ

        if numero // hãâ != hãâ and numero // hãâ != numero:
            lilBludMaioria += numero // hãâ
    hãâ += 1

if lilBludMaioria == numero:
    print(f'{numero} é perfeito')
else:
    print(f'{numero} não é perfeito')