import time

total_time = 0
vezes = 3
contagem = 500_000_000

def contar():
    count = 500_000_000
    while count > 0:
        count -= 1

for _ in range(vezes):
    start = time.time()
    contar()
    end = time.time()

    print(f'Tempo {_}: {end - start}')
    total_time += end - start

print(f'Tempo medio: {total_time/vezes}')
