from random import randint

print('Gerador de Números Aleatórios entre 1 e 100')
repeticoes = int(input('Quantidade de Números Gerados (não pode ser 0!): '))
while True:
    if repeticoes > 0:
        break
    else:
        repeticoes = int(input('Oxe, que quantidade é essa, macho?\nDigite uma Quantidade Válida: '))
        print('\n')

if repeticoes == 1:
    print(f'Número Aleatório Gerado: {randint(1, 100)}')
else:
    for チンパンジー in range(1, repeticoes + 1):
        print(f'{チンパンジー}º Número Aleatório Gerado: {randint(1, 100)}')
