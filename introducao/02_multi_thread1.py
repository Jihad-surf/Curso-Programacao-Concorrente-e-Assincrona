from threading import Thread
import time

total_time = 0
vezes = 3
contagem = 500_000_000

def contar():
    count = contagem
    while count > 0:
        count -= 1

start = time.time()
t = Thread(target=contar, args=())
t2 = Thread(target=contar, args=())
t3 = Thread(target=contar, args=())

t.start()
t2.start()
t3.start()
t.join()
t2.join()
t3.join()

end = time.time()
total_time = end - start

print(f'Tempo total: {total_time}')
print(f'Tempo medio: {total_time/vezes}')

