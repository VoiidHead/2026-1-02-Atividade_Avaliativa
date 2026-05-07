numero = int(input('Digite um número inteiro positivo: '))

soma = 0

for i in range(1,numero+1):
    if numero % i == 0 and i != numero:
        soma += i

if soma == numero:
    print(f'{numero} é perfeito')
else:
    print(f'{numero} não é perfeito')