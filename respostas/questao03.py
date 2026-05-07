from math import sqrt

print('Seu Número É Perfeito?')
numero = int(input('Inteiro Positivo: '))
while True:
    if numero > 0:
        break
    else:
        numero = int(input('Tem que ser positivo, pô!\nInteiro Positivo: '))
        print('\n')
lilBludMaioria = []
hãâ = 1

while hãâ <= sqrt(numero):
    if numero % hãâ == 0:
        lilBludMaioria.append(hãâ)
    hãâ += 1

if sum(lilBludMaioria) == numero:
    print(f'{numero} é perfeito')
else:
    print(f'{numero} não é perfeito')