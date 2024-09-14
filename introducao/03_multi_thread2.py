from threading import Thread
import time

def contar_100():
    count = 100_000_000
    while count > 0:
        count -= 1


start = time.time()

threads = []
for _ in range(10):
    t = Thread(target=contar_100, args=())
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
total_time = end - start

print(f'Tempo medio: {total_time/10}')