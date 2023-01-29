import time
from typing import List
from settings import *

def log_update_add(add_id: int, response_code: int, target_cpm: int):
    f = open(Logs.UPDATE_CPM_LOGS, 'a')
    f.write(f"{str(time.ctime())}\tCampaign ID: {str(add_id)}\tresponse code: {str(response_code)}\ttarget cpm: {str(target_cpm)}\tCPM updated: {['FAILURE', 'OK'][response_code == 200]}\n")
    f.close()

def log_cur_positions(cur_positions: List[List[int]], vendor_code: int):
    f = open(Logs.CARD_CPM_LOGS, 'a')
    to_write = f"{str(time.ctime())} vendor code [{vendor_code}]"
    for position in cur_positions:
        to_write += f"\t {str(position[1])}"
    to_write+="\n"
    f.write(to_write)
    f.close()

def log_cur_positions_by_keywords(cur_positions: List[List[int]], words: str):
    f = open(Logs.SEARCH_LOGS, 'a')
    to_write = f"{str(time.ctime())} keywords are [{words}]"
    for position in cur_positions:
        to_write += f"\t {str(position[1])}"
    to_write+="\n"
    f.write(to_write)
    f.close()
