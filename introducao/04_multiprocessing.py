import time
from multiprocessing import Pool

def contar_100(_):
    count = 400_000_000
    while count > 0:
        count -= 1
    
    print('Fim da contagem')

if __name__ == "__main__":
    start = time.time()

    with Pool(12) as p:
        p.map(contar_100, range(10))

    end = time.time()
    total_time = end - start

    print(f'Tempo total: {total_time}')
    print(f'Tempo médio: {total_time/10}')

