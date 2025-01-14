import threading
import time

# fazer a função que conta ate 6, com um intervalo de 1 segundo, duas vezes. Como fazer isso executar mais rapido, isso não é possivel com a abordagem normal, pois o python executa o código de forma sequencial, ou seja, um comando após o outro. Para fazer isso de forma paralela, podemos usar threads.

def count_numbers(thread_name):
    for i in range(1, 7):
        print(f"{thread_name} contando: {i}")
        time.sleep(1)

def main_no_thread():
    start = time.time()
    count_numbers("Thread Um")
    count_numbers("Thread Dois")

    print(f"NORMAL - Contagem finalizada! Tempo total: {time.time() - start}")

def main_thread():
    start = time.time()
    # Criar duas threads
    thread1 = threading.Thread(target=count_numbers, args=("Thread Um",))
    thread2 = threading.Thread(target=count_numbers, args=("Thread Dois",))

    # Iniciar as threads
    thread1.start()
    thread2.start()

    # Esperar que ambas as threads terminem
    thread1.join()
    thread2.join()

    print(f"THREAD - Contagem finalizada! Tempo total: {time.time() - start} \n\n")


if __name__ == "__main__":
    main_thread()
    main_no_thread()