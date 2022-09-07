from copyreg import add_extension
from lib2to3.pgen2 import driver
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
import time
import random

driver = Chrome()
driver.get('https://app.gologin.com/#/sign_in')
email = driver.find_element(By.XPATH, "//input[@placeholder='Email address']")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
email.send_keys('chiendd3@fsoft.com.vn')
password.send_keys('abcxyz123')
submit.click()

# driver.get('https://app.gologin.com/#/profileList')

time.sleep(3)
new_profile_link = driver.find_element(By.LINK_TEXT, 'New Profile')
new_profile_link.click()

time.sleep(2)
overview_tabs = driver.find_elements(By.XPATH, "//div[@role='tab']")
print(overview_tabs)
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
time.sleep(15)

add_extension = driver.find_element(By.XPATH, "//span[text()='Add extensions']")
add_extension_btn = add_extension.find_element(By.XPATH, '..')
# print(add_extension_btn)
add_extension_btn.click()

# time.sleep(15)
# installs = driver.find_elements(By.LINK_TEXT, "Install")



# for i in range(0, random.randint(0, 5)):
#     time.sleep(10)
#     index = random.choice([range(0, len(installs))])
#     installs[index].click()


