import random
r = int(input('Digite a quantidade de números aleatórios: '))
for i in range(1,r+1):
    n = random.randint(1,100)
    print(f'{i}o número aleatório {n}')