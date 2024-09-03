import json
import time
import requests
from datetime import datetime, timedelta, timezone

def get_Token():
    # Загрузка данных из файла config.json
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)
    #
    # # Шаг 2: Обновить значение 'auth_date' на текущее время в формате UNIX timestamp
    # config_data['auth_date'] = str(int(time.time()))
    #
    # # # Шаг 3: Записать обновлённые данные обратно в файл
    # with open('config.json', 'w', encoding='utf-8') as config_file:
    #     json.dump(config_data, config_file, ensure_ascii=False, indent=4)

    url = "https://api.cosmo-miner.com/user/auth"

    payload = json.dumps(config_data)
    print(payload)
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'dnt': '1',
        'ngrok-skip-browser-warning': 'true',
        'origin': 'https://cosmo-miner.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://cosmo-miner.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    return response.get("token")




def start(token):
    url = "https://api.cosmo-miner.com/user/farm/start"

    payload = {}
    headers = {
      'accept': '*/*',
      'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
      'authorization': f'Bearer {token}',
      'cache-control': 'no-cache',
      'content-length': '0',
      'content-type': 'application/json',
      'dnt': '1',
      'ngrok-skip-browser-warning': 'true',
      'origin': 'https://cosmo-miner.com',
      'pragma': 'no-cache',
      'priority': 'u=1, i',
      'referer': 'https://cosmo-miner.com/',
      'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def claim(token):
    url = "https://api.cosmo-miner.com/user/farm/claim"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'dnt': '1',
        'ngrok-skip-browser-warning': 'true',
        'origin': 'https://cosmo-miner.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://cosmo-miner.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


def get_info_farm(token):
    url = "https://api.cosmo-miner.com/user/income"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'dnt': '1',
        'ngrok-skip-browser-warning': 'true',
        'origin': 'https://cosmo-miner.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://cosmo-miner.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    return response.get("lastFarmStart")


def main_loop():
    while True:
        try:
            token = get_Token()
            print(token)
            time_str = get_info_farm(token)
            print(time_str)
            if time_str is None or time_str.strip() == '':
                print("Запускаем Старт")
                # Если время None или пустое (с учетом возможных пробелов), запускаем старт
                start(token)
            else:
                timeStartGame = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
                time_end = timeStartGame + timedelta(hours=8, minutes=2)
                current_time_utc = datetime.now(timezone.utc)

                # Вычисляем оставшееся время до выполнения claim
                time_sleep_sec = int((time_end - current_time_utc).total_seconds())
                if time_sleep_sec <= 0:
                    print("Запускаем клейм")
                    claim(token)
                else:
                    # Ждем оставшееся время
                    print(f"Ожидание {time_sleep_sec} секунд")
                    time.sleep(time_sleep_sec)

        except Exception as e:
            print(f"Произошла ошибка: {e}")
            time.sleep(60)  # Подождем 1 минуту перед повторной попыткой


# Вызов основного цикла
if __name__ == "__main__":
    main_loop()