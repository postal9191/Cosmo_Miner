# main.py

import threading

import Cosmo_Miner  # Импортируем Cosmo_Miner.py
import spin  # Импортируем spin.py



def start_cosmo_thread():
    # Запуск задач Cosmo_Miner в отдельном потоке
    Cosmo_Miner.main_loop()

def start_spin_thread():
    # Запуск задач спина в отдельном потоке
    spin.spinRun()

def main():
    # Создаем и запускаем поток для Cosmo_Miner
    cosmo_thread = threading.Thread(target=start_cosmo_thread)
    cosmo_thread.start()

    # Создаем и запускаем поток для spin
    spin_thread = threading.Thread(target=start_spin_thread)
    spin_thread.start()


if __name__ == "__main__":
    main()
