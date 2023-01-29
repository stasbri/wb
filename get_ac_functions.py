from settings import *
import requests
from typing import Dict, List
import json

def get_ac_by_vendor_code(code: int) -> requests.Response:
    res: requests.Response = requests.get(url=LINK_FOR_RANDOM_SITE + str(code))
    return res

def get_prices_and_places_by_vendor_code(code: int) -> List[List[int]]:
    res = list()
    adds = get_ac_by_vendor_code(code).json()
    for i in range(len(adds)):
        res.append([0, 0])
        res[i][0] = adds[i]["position"]
        res[i][1] = adds[i]["cpm"]
    return res

def get_ac_by_keywords(words:str):
    splitted = words.split()
    part_of_link = splitted[0]
    for i in range(1, len(splitted)):
        part_of_link += "%20"
        part_of_link+= splitted[i]
    res = requests.get(url=OTHER_RANDOM_LINK + part_of_link)
    return res

def get_prices_and_places_by_keywords(words: str) -> List[List[int]]:
    res = list()
    adds = get_ac_by_keywords(words).json()["adverts"]
    for i in range(len(adds)):
        res.append([0, 0])
        res[i][0] = i + 1
        res[i][1] = adds[i]["cpm"]
    return res