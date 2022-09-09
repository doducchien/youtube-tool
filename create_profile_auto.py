from undetected_chromedriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import time
import random

import threading
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

list_total_count = []

def exit_when_error(driver, number_thread, e):
    print("Thread ", number_thread, "Oops!", e.__class__, "occurred.")
    print("Thread ", number_thread, "Create profile fail!")
    driver.close()
    driver.quit()

def try_hard(lock, number_thread):
    target_account = 30
    current_account = 0
    while (current_account < target_account):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = Chrome(options=options)
        driver.get('https://app.gologin.com/#/sign_in')
        driver.implicitly_wait(5)
        try:
            w = WebDriverWait(driver, 15)
            w.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email address']")))
            w.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
            w.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        except Exception as e: 
            print("Thread {}: Dont find some inputs".format(number_thread))
            exit_when_error(driver, number_thread, e)
            continue


        email = driver.find_element(By.XPATH, "//input[@placeholder='Email address']")
        password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        email.send_keys('chiendd3@fsoft.com.vn')
        time.sleep(2)
        password.send_keys('abcxyz123')
        time.sleep(2)
        submit.click()
        try:

            w = WebDriverWait(driver, 7)
            w.until(EC.presence_of_element_located((By.LINK_TEXT, 'New Profile')))
        except Exception as e: 
            print("Thread ", number_thread, "go to home wrong")
            exit_when_error(driver, number_thread, e)
            continue
        for i in range(target_account):
            time.sleep(4)
            new_profile_link = driver.find_element(By.LINK_TEXT, 'New Profile')
            new_profile_link.click()

            time.sleep(2)
            try:
                w = WebDriverWait(driver,10)
                w.until(EC.presence_of_element_located((By.XPATH, "//div[@role='tab']")))
            except Exception as e:
                print("Thread ", number_thread, "dont find tab")
                exit_when_error(driver, number_thread, e)


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
            try:
                w = WebDriverWait(driver,20)
                w.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Add extensions']")))
            except Exception as e:
                print("Thread ", number_thread, "dont find Add extensions")
                exit_when_error(driver, number_thread, e)

            add_extension = driver.find_element(By.XPATH, "//span[text()='Add extensions']")
            add_extension_btn = add_extension.find_element(By.XPATH, '..')
            add_extension_btn.click()
            time.sleep(12)
            try:

                w = WebDriverWait(driver, 10)
                w.until(EC.presence_of_element_located((By.LINK_TEXT, "Install")))
            except Exception as e:
                print("Thread ", number_thread, "go to home wrong")
                exit_when_error(driver, number_thread, e)
            time.sleep(4)
            installs = driver.find_elements(By.LINK_TEXT, "Install")
            time.sleep(3)


            index_selected = -1
            for i in range(0, random.randint(0, 4)):
                index = random.randrange(0, 50)
                while index == index_selected:
                    index = random.randrange(0, 50)
                index_selected = index
                installs[index_selected].find_element(By.XPATH, '..').click()
                time.sleep(3)

            close_btn = driver.find_element(By.CLASS_NAME, 'ant-modal-close')
            close_btn.click()

            time.sleep(3)
            create_profile_btn = driver.find_element(By.XPATH, "//span[text()='Create Profile']").find_element(By.XPATH, '..')
            create_profile_btn.click()
            current_account += 1
            list_total_count[number_thread] = current_account
            print("Thread ", number_thread, "Create profile success!")
            print("Thread ", number_thread, "Number account success is: {}".format(current_account))


            time.sleep(10)
        driver.close()
        driver.quit()

if __name__ == "__main__":
    count = 0

    lock = threading.Lock()
    total_thread = 2
    list_thread = []
    for i in range(total_thread):
        list_thread.append(threading.Thread(target=try_hard, args=(lock,i)))
        list_total_count.append(0)

    for thread_item in list_thread: thread_item.start()
    for thread_item in list_thread: thread_item.join()

    
    print("FINISH", "TOTAL:", sum(list_total_count))


    

