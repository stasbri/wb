from settings import *
from functions import *
import requests



if __name__ == "__main__":
    r = get_my_ac_list()
    rr = get_my_ACs()
    print_pretty(r)
    print_pretty(rr)