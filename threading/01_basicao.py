"""Mostrar o básico de como criar e iniciar uma thread em Python. E mostrar ela executando em paralelo com o código principal."""

import threading
import time

def enviar_mensagens(mensages):
    for mensagem in mensages:
        print(mensagem)
        time.sleep(1)  # Simula um pequeno atraso
"""
enviar_mensagens(["Olá!", "Tubo bem?", "Pode me chamar de Python!", "O que você está fazendo?"])

print("Fazendo outra coisa...")
time.sleep(2)
print("Acabou!")
"""


# Criar uma thread com uma lista de mensagens
thread = threading.Thread(target=enviar_mensagens, args=(["Olá!", "Tubo bem?", "Pode me chamar de Python!", "O que você está fazendo?"],))

# Iniciar a thread
thread.start()
print("Fazendo outra coisa...")
time.sleep(2)
print("Acabei de fazer outra coisa!")

# Esperar que a thread termine
thread.join()
print("Acabou!")
