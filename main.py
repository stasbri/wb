from settings import *
from functions import *
import time
import requests



if __name__ == "__main__":
    for i in range(0, 1236):
        print(i)
        resp = get_all_ac_list(6, 1234)
        print(resp.status_code)
        print_pretty(resp)
        time.sleep(2)