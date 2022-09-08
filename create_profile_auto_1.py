from copyreg import add_extension
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import time
import random

import threading
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

count = 0


def try_hard(lock):

    driver = Chrome()
    driver.get('https://app.gologin.com/#/sign_in')
    email = driver.find_element(By.XPATH, "//input[@placeholder='Email address']")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    email.send_keys('chiendd3@fsoft.com.vn')
    password.send_keys('abcxyz123')
    submit.click()
    for i in range(30):
        try:
            time.sleep(4)
            new_profile_link = driver.find_element(By.LINK_TEXT, 'New Profile')
            new_profile_link.click()

            time.sleep(2)
            overview_tabs = driver.find_elements(By.XPATH, "//div[@role='tab']")
            overview = overview_tabs[0]
            extension = overview_tabs[3]
            overview.click()
            time.sleep(1)
            window = driver.find_element(By.XPATH, "//span[text()='Windows']")
            window.click()
            time.sleep(1)
            new_finger = driver.find_element(By.XPATH, "//span[text()='New Fingerprint']")
            button_new_finger = new_finger.find_element(By.XPATH, '..')
            button_new_finger.click()


            time.sleep(1)
            extension.click()
            time.sleep(20)

            add_extension = driver.find_element(By.XPATH, "//span[text()='Add extensions']")
            add_extension_btn = add_extension.find_element(By.XPATH, '..')
            add_extension_btn.click()
            time.sleep(12)
          
            installs = driver.find_elements(By.LINK_TEXT, "Install")
            time.sleep(3)



            for i in range(0, random.randint(0, 4)):
                index = random.randrange(0, 50)
                installs[index].click()
                time.sleep(3)

            close_btn = driver.find_element(By.CLASS_NAME, 'ant-modal-close')
            close_btn.click()

            time.sleep(1)
            create_profile_btn = driver.find_element(By.XPATH, "//span[text()='Create Profile']").find_element(By.XPATH, '..');
            create_profile_btn.click()
            print("Create profile success!")
            lock.acquire()
            global count
            count += 1
            print("Number account success is: {}".format(count))
            lock.release()
            time.sleep(10)
        except Exception as e: 
            print("Oops!", e.__class__, "occurred.")
            print("Create profile fail!")
    driver.close()

if __name__ == "__main__":
    count = 0

    lock = threading.Lock()
    t1 = threading.Thread(target=try_hard, args=(lock,))
    t2 = threading.Thread(target=try_hard, args=(lock,))
    t3 = threading.Thread(target=try_hard, args=(lock,))
    #t4 = threading.Thread(target=try_hard, args=(lock,))

    t1.start()
    t2.start()
    t3.start()
    #t4.start()


    t1.join()
    t2.join()
    t3.join()
    #t4.join()
    
    print("FINISH")


    

