import time

total_time = 0

def contar_100():
    count = 900_000_000
    while count > 0:
        count -= 1

for _ in range(1):
    start = time.time()
    contar_100()
    end = time.time()

    print(f'Tempo {_}: {end - start}')
    total_time += end - start

print(f'Tempo medio: {total_time/3}')
