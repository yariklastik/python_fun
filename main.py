import requests

with open('site.txt', 'r') as file:
    links = [line.strip() for line in file]

for link in links:
    try:
        response = requests.get(link)
        status_code = response.status_code

        if 200 <= status_code < 300:
            print(f'(ОК): {link}')
        elif 400 <= status_code < 500:
            print(f'(НЕ ОК): Ресурс "{link}" не відповідає')
        else:
            print(f'(НЕ ОК): Невідомий статус код {status_code} для {link}')
    except requests.exceptions.RequestException as e:
        print(f'(Помилка): Помилка при виконанні запиту для {link}: {e}')
