from settings import *
import requests
from typing import Dict
import json

def get_my_ACs() -> requests.Response:
    res: requests.Response = requests.get(url=MY_ACs, headers=authorization_header)
    return res

def get_my_ac_list() -> requests.Response:
    res: requests.Response = requests.get(url=MY_AC_LIST, headers=authorization_header)
    return res

def get_all_ac_list(ac_type: int) ->requests.Response:
    params: Dict =  {
                        'type' : str(ac_type),
                        'param' : '1234'
                    }
    res: requests.Response = requests.get(url=ALL_ADS_LIST, params=params, headers=authorization_header)
    return res

def print_pretty(arg:requests.Response):
    print(json.dumps(json.loads(arg.text), indent=4))