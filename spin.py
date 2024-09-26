import time
from datetime import datetime, timedelta, timezone

import requests
import tokenFefresh

headersReklama = {
        'Accept': '*/*',
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://cosmo-miner.com',
        'Referer': 'https://cosmo-miner.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }


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
    # print(response.text)

    if response.text:  # Проверяем, что ответ не пустой
        try:
            prize = response.json().get('prize')
            if prize is not None:  # Проверяем, что значение 'prize' не None
                print(prize)
            else:
                print("Что-то пошло не так: значение 'prize' отсутствует.")
        except requests.exceptions.JSONDecodeError:
            print("Ошибка декодирования JSON: неверный формат ответа.")
    else:
        print("Что-то пошло не так: ответ пустой.")

def reklamaGet():

    url = "https://api.adsgram.ai/adv?blockId=306&tg_id=1249648420&tg_platform=tdesktop&platform=Win32&language=ru&is_premium=true" # тут tg_id заменить на свой

    payload = {}

    response = requests.request("GET", url, headers=headersReklama, data=payload).json()
    # print(response)
    return response

def blockReklama():
    dataRekl = reklamaGet()
    payload = {}

    render = dataRekl['banner']['trackings'][0]['value']
    requests.request("GET", render, headers=headersReklama, data=payload).json()

    time.sleep(3)
    show = dataRekl['banner']['trackings'][1]['value']
    requests.request("GET", show, headers=headersReklama, data=payload).json()

    time.sleep(3)
    reward = dataRekl['banner']['trackings'][3]['value']
    requests.request("GET", reward, headers=headersReklama, data=payload).json()

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
            blockReklama() # тест автопроталкивание рекламы

            print('Суточный лимит спинов осталось ', maxSpins - todaySpinsCount, )
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
