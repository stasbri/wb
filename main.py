from settings import *
from functions import *
import requests



if __name__ == "__main__":
    r = get_all_ac_list(5)
    print_pretty(r)
    r = get_all_ac_list(6)
    print_pretty(r)
    r = get_all_ac_list(7)
    print_pretty(r)
    r = get_all_ac_list(4)
    print_pretty(r)