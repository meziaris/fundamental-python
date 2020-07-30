import requests

try:
    response = requests.get('https://mezi.space')
    if response.status_code == 200:
        print(f'Success! Response Code = {response.status_code}')
        print(response.text)
    else:
        print(f'Woops, something wrong! error {response.status_code}')
except Exception as e:
    print(f'There is an erro {e}')
