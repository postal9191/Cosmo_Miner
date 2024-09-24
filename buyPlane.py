import time

import requests
import json


def buyPlane50k(token):

    url = "https://api.cosmo-miner.com/user/buy/card"

    payload = json.dumps({
      "id": "666c1e587b26f2ded2688622"
    })
    headers = {
      'accept': '*/*',
      'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
      'authorization': f'Bearer {token}',
      'content-type': 'application/json',
      'ngrok-skip-browser-warning': 'true',
      'origin': 'https://cosmo-miner.com',
      'priority': 'u=1, i',
      'referer': 'https://cosmo-miner.com/',
      'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def buyMultiplePlanes(current_coins, token):
    # Проверяем, что текущие монеты положительные
    print(f'Количество монет {current_coins}')

    if current_coins < 50000:
        print("Количество монет меньше нужного.")


    # Рассчитываем, сколько самолётов можно купить (целое число)
    number_of_planes = current_coins // 50000
    print(f'Купим {number_of_planes} кораблей')
    # Запускаем функцию buyPlane50k нужное количество раз
    for _ in range(number_of_planes):
        buyPlane50k(token)
        time.sleep(10)
