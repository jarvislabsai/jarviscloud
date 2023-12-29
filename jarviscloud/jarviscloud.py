import requests
import urllib3
from pathlib import Path
urllib3.disable_warnings()


path = Path('/home/.jarviscloud/jarvisconfig')
url = 'https://backend.jarvislabs.net'


def pause():
    # token, id, user_id = path.open().read().split()
    token, id, user_id, machine_name = path.open().read().strip().split('\n')
    if len(token) > 100:
        requests.post(f'{url}/pause',
                      json={'jwt': token, 'id': id}, verify=False)
    else:
        requests.post(f'{url}/pause',
                      json={'jwt': token, 'id': id, 'user_id': user_id}, verify=False)


def destroy():
    # token, id, user_id = path.open().read().split()
    token, id, user_id, machine_name = path.open().read().strip().split('\n')
    if len(token) > 100:
        requests.post(f'{url}/destroy',
                      json={'jwt': token, 'id': id}, verify=False)
    else:
        requests.post(f'{url}/destroy',
                      json={'jwt': token, 'id': id, 'user_id': user_id}, verify=False)
