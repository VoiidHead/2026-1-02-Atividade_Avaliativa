print('Informações Sobre Seu Conjunto de Inteiros Positivos')
repeticoes = int(input('Para criar Seu Conjunto, Digite a Quantidade de Elementos que Ele Terá.\nQuantidade: '))
fazmestre = input('Nome do Seu Conjunto: ')
while True:
    try:
        int(fazmestre)
        fazmestre = input('Não Pode Ser um Número\nNome do Conjunto: ')
    except ValueError:
        print('\n')
        break

while True:
    if repeticoes > 0:
        break
    else:
        repeticoes = int(input('Oxe, pae, que quantidade é essa?\nDigite uma Quantidade Válida: '))
        print('\n')
Euclides = []
kvanta = 1

while repeticoes != 0:
    heehee = int(input(f'Digite seu valor {kvanta} (deve ser um inteiro): '))
    Euclides.append(heehee)
    kvanta += 1
    repeticoes -= 1

print('\n', fazmestre, '=', Euclides, '\n')
print(f'Soma dos Elementos do Conjunto {fazmestre}: {sum(Euclides)}')
print(f'Média dos Elementos do Conjunto {fazmestre}: {(sum(Euclides) / kvanta)}')
print(f'Maior Elemento do Conjunto {fazmestre}: {max(Euclides)}')
print(f'Menor Elemento do Conjunto {fazmestre}: {min(Euclides)}')
elementalmenteGulosos = []
for ÓOSA in Euclides:
    if ÓOSA > sum(Euclides) / kvanta:
        elementalmenteGulosos.append(ÓOSA)
print(f'Conjunto de Elementos Maiores Que a Média no Conjunto {fazmestre}: {elementalmenteGulosos}')
