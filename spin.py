import time
from datetime import datetime, timedelta, timezone

import requests
import tokenFefresh

def get_info_spin(get_Token):
    url = "https://api.cosmo-miner.com/spin"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {get_Token}',
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
    # print(response) #debug
    return response


def spin(get_Token):
    url = "https://api.cosmo-miner.com/spin"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {get_Token}',
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

    print(response.json()['message'])


def spinRun():
    while True:
        token = tokenFefresh.get_Token()

        countSpin = get_info_spin(token)
        freeSpins = countSpin.get('freeSpins')
        adCombo = countSpin.get('adCombo')
        maxSpins = countSpin.get('maxSpins')
        todaySpinsCount = countSpin.get('todaySpinsCount')
        lastSpinDate = countSpin.get('lastSpinDate')

        # Преобразуем lastSpinDate в объект datetime
        lastSpinDate = datetime.fromisoformat(lastSpinDate.replace('Z', '+00:00'))
        current_time = datetime.now(timezone.utc)
        wait_time = int((lastSpinDate + timedelta(minutes=10) - current_time).total_seconds())

        # Проверяем, прошло ли больше 10 минут с последнего спина
        if wait_time > 0:
            print(f"Ждем {wait_time} секунд чтобы крутить спины снова")
            time.sleep(wait_time)

        # После ожидания проверяем количество оставшихся спинов
        if todaySpinsCount < maxSpins:
            print('Осталось спинов на сегодня', maxSpins - todaySpinsCount, )
            spins_to_perform = freeSpins + adCombo
            if spins_to_perform == 0:
                print("Нет доступных спинов. Ожидание 30 минут перед перезапуском цикла.")
                time.sleep(1800)  # 1800 секунд = 30 минут
                continue
            print(f"Будем выполнять spin {spins_to_perform} раза с задержкой в 10 секунд")
            for _ in range(spins_to_perform):
                spin(token)
                time.sleep(10)
        else:
            # Если сегодня уже потрачено максимальное количество спинов, ждем следующего дня
            next_day = (current_time + timedelta(days=1)).replace(hour=0, minute=5, second=0, microsecond=0)
            wait_time = (next_day - current_time).total_seconds()
            print(f"Ждем до следующего дня: {wait_time} секунд для вращения спинов")
            time.sleep(wait_time)


if __name__ == "__main__":
    spinRun()
