from settings import *
import requests

if __name__ == "__main__":
    print(URL)
    print(authorization_header)
    r = requests.get(url=URL, headers=authorization_header)
    print(r.json())
