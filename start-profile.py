import json
from multiprocessing import Pool, freeze_support
from urllib import request
from pygologin.gologin import GoLogin
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import requests
import time
import os
# gl = GoLogin({
#     'token': '1eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzE4Nzg0ZjYyY2RiZDZlYTQzNTZmOGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzE4OGNjMWUzNGIwODIyMGE2ZWRjOWIifQ.whKBz_jbenkPCj_Hw5Wdqybgc7PTn_SOnkSOK9l_kag',
#     'profile_id': '63187ab57addf177e54cb465'
# })


# print(type(gl))
# debugger_address = gl.start()
# print("debugger_address:", debugger_address)

# for property in [a for a in dir(debugger_address) if not a.startswith('__')]:
#     print("{}: {}".format(gl, getattr(gl, property)))
# gl.stop()


# if __name__ == "__main__":
#     print(debugger_address)

def fetch_profiles(page, size):
    url = '{}/profiles?page={}&size={}'.format(
        "http://localhost:2024", page, size)
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['data']['listItem']


profiles = fetch_profiles(0, 5000)
def start(profile):
    try:
        gl = GoLogin({
            'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzFlNWU5MzgzZDVlZTQzNDVjYjQ0N2IiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzFlNWVmMDM3MGJkMzQ1ZGM1NWQ1NmYifQ.2esEh_omsLb6a9wI6TkrwsD_CG0LiFs9TvDjn8-0Jvg',
            'profile_id': profile['id']
        })
        gl.start()
        return 1
    except Exception as e:
        print("error:",e)
        return 0

total_profile = 0
if __name__ == '__main__':
    i = 1660
    while i < 5000:
        with Pool(8) as p:
            result = p.map(start, profiles[i: i + 10])
        i+=10   
        time.sleep(20)
        total_profile += sum(result)
        print('Current profiles:', total_profile)
        os.system("TASKKILL /f  /IM  CHROME.EXE")
        os.system("TASKKILL /f  /IM  CHROMEDRIVER.EXE")


    print("Total profile is", total_profile)


start(profiles[0])