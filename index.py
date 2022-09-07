from lib2to3.pgen2 import driver
from random import random
from undetected_chromedriver import Chrome, ChromeOptions;
from selenium.webdriver.common.by import By
import os
import time
import random

list_time = [2,3,4,5]
list_time_wait = [60, 70, 80]

def changeIp():
    cmd_connect = 'rasdial Chien'
    cmd_disconnect = 'rasdial/disconnect'
    os.system(cmd_disconnect)
    time.sleep(4)
    os.system(cmd_connect)
    time.sleep(4)


url = 'https://www.youtube.com/watch?v=sikJJxC7A6Q&t=21s'

for i in range(20):
    changeIp()
    options = ChromeOptions()
    options.add_extension('extension/fhkphphbadjkepgfljndicmgdlndmoke.crx')
    options.add_extension('extension/lanfdkkpgfjfdikkncbnojekcppdebfp.crx')
    options.add_extension('extension/olnbjpaejebpnokblkepbphhembdicik.crx')
    options.add_extension('extension/pcbjiidheaempljdefbdplebgdgpjcbe.crx')

    options.add_experimental_option('debuggerAddress', )

    driver = Chrome(options=options)

    time.sleep(random.choice(list_time))
    try:
        driver.get(url)
        player = driver.find_element(By.ID, 'player')
        time.sleep(random.choice(list_time))
        player.click()
        time.sleep(list_time_wait)
        driver.close()
    except:
        print("error")

