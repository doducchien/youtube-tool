import multiprocessing
from random import random
from re import S
import signal
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os
import time
import random
import requests
import json
import threading
from pygologin.gologin import GoLogin
from sys import platform

localhost = 'http://localhost:2024'
url = 'https://www.youtube.com'
size = 4
page = 0

path_chrome = 'C:\\Users\\cinterface\\.gologin\\browser\\orbita-browser\\chrome.exe --remote-debugging-port={} --user-data-dir=C:\\Users\\cinterface\\AppData\\Local\\Temp\\gologin_{}'

def changeIp():
    print("Changing ip address...")
    cmd_connect = 'rasdial chien'
    cmd_disconnect = 'rasdial/disconnect'
    os.system(cmd_disconnect)
    time.sleep(5)
    os.system(cmd_connect)
    time.sleep(10)





def fetch_profiles():
    url = '{}/profiles?page={}&size={}'.format(localhost, 0, 4600)
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['data']['listItem']

def try_hard(profile):
    pid = os.getpid()
    port = profile['port']
    id = profile['id']
    driver_exe = profile['driver']
    debugger_address = '127.0.0.1:{}'.format(port)
    p = subprocess.Popen(path_chrome.format(port, id), stdout=subprocess.PIPE, shell=True)
    try:
        time.sleep(2)
        print('debugger_address: ',debugger_address)
        options = Options()
        options.add_experimental_option('debuggerAddress', debugger_address)
        driver = Chrome(executable_path= driver_exe, options=options)
        driver.get(url)
        time.sleep(18)
        try:
            search = driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm']")
            print(search)
            time.sleep(2)
            search.send_keys('pubg mobile đứng trên mái nhà')
            search_icon = driver.find_element(By.ID, 'search-icon-legacy')
            time.sleep(2)
            search_icon.click()
            time.sleep(7)
        except Exception as e:
            print("eee:", e)
        count = 0 
        while count < 10:
            try:
                my_video = driver.find_element(By.XPATH, '//a[@href="/watch?v=VuY5rVmlMyI"]')
                my_video.click()
                break
            except Exception as e:
                print('e1:', e)
                count+=1

        # count = 0
        # while count < 10:

        #     try:
        #         play_btn = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
        #         time.sleep(2)
        #         play_btn.click()
        #         break
        #     except: 
        #         print('No found play button')
        #         count += 1
        #         if count == 5: 
        #             driver.close()
        #             p.terminate()
        #             return 0


        time.sleep(250)     
        driver.close()
        return 1
    except Exception as e:
        print("exception:", e)
        p.terminate()
        return 0

profiles = fetch_profiles()
ports = [22006, 22007, 22008, 22009, 22010, 22011, 22012, 22013, 22014, 22015]
drivers = ['c1.exe', 'c2.exe', 'c3.exe', 'c4.exe']
def mapPortToProfile(port, profile, driver):
    profile['port'] = port
    profile['driver'] = driver
    return profile

if __name__ == '__main__':
    multiprocessing.freeze_support()
    i = 700
    total_view = 0
    while True:
        if i == 4600: break
        changeIp()
        with multiprocessing.Pool(4) as p:
            mappedProfiles = map(mapPortToProfile, ports, profiles[i: i + 4], drivers)
            result = p.map(try_hard, mappedProfiles)
        total_view += sum(result)
        i+= 5
        os.system("TASKKILL /f  /IM  CHROME.EXE")
        os.system("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
        print("Current view is:", total_view)
    
    print("DONE! total view is:", total_view)