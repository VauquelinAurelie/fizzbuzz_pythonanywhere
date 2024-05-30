import subprocess

import requests

username = 'vauquelinAurelie'
token = '4ba5207256b2669e1972f4835dec72241f397cc0'
console_id = 34033938
url = 'vauquelinAurelie.pythonanywhere.com'
response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

result = subprocess.run(["pytest"], shell=True, capture_output=True, text=True)


def pushongit():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "test ok"])
    subprocess.run(["git", "push", "origin", "main"])


def pull_on_server():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{console_id}/send_input'.format(
            username=username,
            console_id=console_id
        ),
        headers={'Authorization': 'Token {token}'.format(token=token),
                 'Content-Type': 'application/json'},
        json={"input: cd ~/mysite && git pull/n"}
    )


def reload_on_server():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/wabapps/{url}/reload'.format(
            username=username,
            url=url
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )


if result.returncode:
    print("test invalide")
else:
    print("test ok")
    pushongit()
    pull_on_server()
    reload_on_server()
