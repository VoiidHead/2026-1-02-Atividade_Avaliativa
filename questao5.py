repeticoes = int(input('Digite a quantidade de números: '))

numeros = []
soma = 0
maior = 0
menor = float('inf')
quant = 0

for i in range(1, repeticoes+1):
    numero = int(input(f'Informe o valor {i}: '))
    numeros.append(numero)

for numero in numeros:
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = soma / repeticoes

for numero in numeros:
    if numero > media:
        quant += 1

print(f'a soma total é {soma}')
print(f'a média é {media}')
print(f'o maior valor é {maior}')
print(f'o menor valor é {menor}')
print(f'a quantidade de valores acima da média é {quant}')

    