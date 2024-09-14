from threading import Thread
import time

total_time = 0

def contar_100():
    count = 100_000_000
    while count > 0:
        count -= 1

start = time.time()
t = Thread(target=contar_100, args=())
t2 = Thread(target=contar_100, args=())

t.start()
t2.start()
t.join()
t2.join()

end = time.time()
total_time = end - start

print(f'Tempo total: {total_time}')
print(f'Tempo medio: {total_time/2}')

