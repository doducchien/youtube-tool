from random import random
from undetected_chromedriver import Chrome, ChromeOptions;
from selenium.webdriver.common.by import By
import os
import time
import random
import requests
import json
import threading
from pygologin.gologin import GoLogin

list_time = [2,3,4,5]
list_time_wait = [60, 70, 80]
localhost = 'http://localhost:2024'
url = 'https://www.youtube.com/watch?v=dd4oV9pLL4c&list=PLiHcN6JFj2GoncrnWMES7hfUbbVWOCZnF'
size = 1
page = 160
success_count_thread = 0
list_view = []
def changeIp():
    print("Changing ip address...")
    cmd_connect = 'rasdial chien'
    cmd_disconnect = 'rasdial/disconnect'
    os.system(cmd_disconnect)
    time.sleep(5)
    os.system(cmd_connect)
    time.sleep(10)

    response = requests.get('https://api.myip.com/')
    json_data = json.loads(response.text)
    print("IP address was changed!", json_data['ip'])
    time.sleep(4)






def fetch_profiles(page):
    url = '{}/profiles?page={}&size={}'.format(localhost, page, size)
    response = requests.get(url)
    json_data = json.loads(response.text)
    # print(json_data)

    return json_data['data']['listItem']

def try_hard(thread_id, lock):
    lock.acquire()
    global page
    profiles = fetch_profiles(page)
    page = page - 1
    lock.release()
    print('thread-', thread_id,'-id:', profiles[0]['id'], '-', profiles[0]['data']['name'])
    gl = GoLogin({
        'token': '123',
        'profile_id': profiles[0]['id']
    })
    debugger_address = gl.start()
    options = ChromeOptions()
    options.add_experimental_option('debuggerAddress', debugger_address)
    driver = Chrome(options=options)

    # time.sleep(random.choice(list_time))
    try:
        driver.get(url)
        driver.implicitly_wait(8)
        try:
            play_btn = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
            play_btn.click()
        except: print('No found play button')
        # player = driver.find_element(By.ID, 'player')
        time.sleep(random.randint(60, 80))
        # player.click()
        list_view[i] += 1
        driver.close()
        time.sleep(3)

        gl.stop()
        print("Thread-", thread_id, "-view:", list_view[i])
    except Exception as e:
        driver.close()
        time.sleep(3)
        print("error: ", e)
        gl.stop()


if __name__ == '__main__':
    for i in range(100):
        changeIp()
        lock = threading.Lock()
        total_thread = 3
        list_thread = []
        for i in range(total_thread):
            list_thread.append(threading.Thread(target=try_hard, args=(i, lock)))
            list_view.append(0)

        for thread_item in list_thread: thread_item.start()
        for thread_item in list_thread: thread_item.join()
        time.sleep(5)
    

    print("DONE")