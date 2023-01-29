import time
from typing import List
from settings import LOGS_LOCATIONS

def log_update_add(add_id: int, response_code: int, target_cpm: int):
    f = open(LOGS_LOCATIONS + "updatecpm" + str(add_id) +".log", 'a')
    f.write(f"{str(time.ctime())}\tCampaign ID: {str(add_id)}\tresponse code: {str(response_code)}\ttarget cpm: {str(target_cpm)}\tCPM updated: {['FAILURE', 'OK'][response_code == 200]}\n")
    f.close()

def log_cur_positions(cur_positions: List[List[int]], vendor_code: int):
    f = open(LOGS_LOCATIONS + "current_places" + str(vendor_code) + ".log", 'a')
    to_write = str(time.ctime())
    for position in cur_positions:
        to_write += f"\t {str(position[1])}"
    to_write+="\n"
    f.write(to_write)
    f.close()

def log_cur_positions_by_keywords(cur_positions: List[List[int]], words: str):
    f = open(LOGS_LOCATIONS + "current_places_by_keywords" + words + ".log", 'a')
    to_write = str(time.ctime())
    for position in cur_positions:
        to_write += f"\t {str(position[1])}"
    to_write+="\n"
    f.write(to_write)
    f.close()
