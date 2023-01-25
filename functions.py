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

def get_my_ac_by_id(ac_id: int) -> requests.Response:
    parameters: Dict =  {
                            'id' : str(ac_id)
                        }
    res: requests.Response = requests.get(url=MY_AC_BY_ID, params=parameters, headers=authorization_header)
    return res


def get_all_ac_list(ac_type: int, param: int=1234) -> requests.Response:
    parameters: Dict =  {
                        'type' : str(ac_type),
                        'param' : str(param)
                    }
    res: requests.Response = requests.get(url=ALL_ADS_LIST, params=parameters, headers=authorization_header)
    return res

def print_pretty(arg:requests.Response):
    print(json.dumps(json.loads(arg.text), indent=4))