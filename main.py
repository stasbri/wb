from settings import *
from functions import *
import time
import requests



if __name__ == "__main__":
    r = get_all_ac_list(5)
    while True:
        resp = get_all_ac_list(5)
        if resp.text != r.text:
            print(time.ctime())
            print_pretty(resp)
            r = resp
        time.sleep(2)