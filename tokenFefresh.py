import json
import time
import simplejson
import requests

def get_Token():
    # Загрузка данных из файла config.json
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    url = "https://api.cosmo-miner.com/user/auth"

    payload = json.dumps(config_data)
    # print(payload)
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

    while True:
        try:
            # Выполняем запрос POST
            response = requests.request("POST", url, headers=headers, data=payload)

            # Проверяем, является ли содержимое ответа корректным JSON
            if response.text:
                try:
                    # Пытаемся декодировать JSON
                    json_data = response.json()
                    # Если JSON успешно декодирован, возвращаем токен
                    return json_data.get("token")
                except simplejson.errors.JSONDecodeError:
                    print("Ошибка: получен невалидный JSON. Повтор запроса через 10 секунд.")
            else:
                print("Ошибка: получен пустой ответ. Повтор запроса через 10 секунд.")

        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}. Повтор запроса через 10 секунд.")

        # Задержка перед следующим запросом
        time.sleep(10)
