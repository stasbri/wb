from settings import *
from functions import *
from get_ac_functions import *
import time
import requests
import log_functions

# 4240101

my_ids = [4294873, 4294571, 4285403, 4240101]
subject_id = 168
set_id = 224
test_id = 4240101

def looper():
    while True:
        log_functions.log_update_add(test_id, update_add(test_id, new_price=10, id_type=5, id_param=224), 10)
        log_functions.log_cur_positions(get_prices_and_places_by_vendor_code(142818303), 142818303)
        log_functions.log_cur_positions_by_keywords(get_prices_and_places_by_keywords("куртка весенняя женская"), "куртка весенняя женская")
        time.sleep(60)


if __name__ == "__main__":
        # # resp = get_ac_by_keywords("куртка весенняя женская")
        # resp = get_prices_and_places_by_keywords("куртка весенняя женская")
        # print(resp)
        # print_pretty(resp)
    looper()

