import requests
import threading

# mostrar como criar inumeras threads ao mesmo tempo  


def get_address(cep):
    try:
        response = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        if response.status_code == 200:
            data = response.json()
            print(f"CEP {cep} encontrado!")
        else:
            print(f"CEP {cep} não encontrado!")
        print('\n')
    except Exception as e:
        print(f"Erro ao consultar CEP {cep}: {e}")


def main(ceps):
    for cep in ceps:
        get_address(cep)


def main_thread(ceps):
    threads = []
    for cep in ceps:
        thread = threading.Thread(target=get_address, args=(cep,))
        threads.append(thread)
        thread.start()

    # Esperar que todas as threads terminem
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    ceps = ["01001000", "01310200", "02011200", "02122000", "03045000", "04094001", "05001000", "06097000", "07082110", "08042010",
    "09012340", "10000000", "11013420", "12001500", "13015200", "14090430", "15035000", "16074190", "17012230", "18015220",
    "19012530", "20031040", "21050270", "22041200", "23010580", "24010050", "25015040", "26040330", "27010000", "28010210",
    "29057070", "30012350", "31010300", "32050400", "33020210", "34010590", "35020000", "36012340", "37030030", "38050620",
    "39080110", "40010310", "41020040", "42010200", "43050650", "44012060", "45030040", "46000000", "47012500", "48010700",
    "49020100", "50031030", "51040970", "52014050", "53030940", "54010520", "55020730", "56040210", "57012200", "58070000",
    "59030100", "60020400", "61010500", "62060040", "63050720", "64020600", "65030030", "66070200", "67010910", "68050270",
    "69020340", "70010100", "71030820", "72060730", "73010400", "74012500", "75060100", "76030700", "77020000", "78030150",
    "79050900", "80010300", "81040750", "82020830", "83020210", "84050670", "85030040", "86010710", "87020600", "88020240",
    "89010900", "90010700", "91040130", "92030570", "93020800", "94020590", "95020700", "96030040", "97040920", "98010560",
    "99030730", "99999999" ]

    #main(ceps)
    main_thread(ceps)
    print("Verificação de todos os CEPs concluída!")
    
