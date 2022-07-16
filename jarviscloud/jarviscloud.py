import requests
import urllib3
from pathlib import Path
urllib3.disable_warnings()


path = Path('/home/.jarviscloud/jarvisconfig')


def pause():
    token, id, user_id = path.open().read().split()
    requests.post('https://backendprod.jarvislabs.ai:8000/pause',
                  json={'jwt': token, 'id': id, 'user_id': user_id}, verify=False)
    
def destroy():
    token, id, user_id = path.open().read().split()
    requests.post('https://backendprod.jarvislabs.ai:8000/destroy',
                  json={'jwt': token, 'id': id, 'user_id': user_id}, verify=False)
