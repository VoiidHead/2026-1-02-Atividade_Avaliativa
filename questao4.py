numero = int(input('Digite um numero inteiro positivo: '))

quant = 0

while numero != 0:
    numero = numero // 10
    quant += 1

print(quant)