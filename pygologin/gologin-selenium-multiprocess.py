import time
import os
from multiprocessing import Pool, freeze_support
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin

def scrap(profile):
	gl = GoLogin({
	        'token': 'yU0token',
	        'profile_id': profile['profile_id'],
	        'port': profile['port'],
		})

	if platform == "linux" or platform == "linux2":
		chrome_driver_path = './chromedriver'
	elif platform == "darwin":
		chrome_driver_path = './mac/chromedriver'
	elif platform == "win32":
		chrome_driver_path = 'chromedriver.exe'

	debugger_address = gl.start()
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", debugger_address)
	driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
	driver.get("http://www.python.org")
	print('ready', profile['profile_id'], driver.title)
	time.sleep(10)
	print('closing', profile['profile_id'])
	driver.close()
	gl.stop()

profiles = [
	{'profile_id': '631adb27695b6700fe16a94f', 'port': 3500}, 
	{'profile_id': '631adad24a802fed34e0d034', 'port': 3501},
	{'profile_id': '631ad9ff58113736c902759f', 'port': 3502},
	{'profile_id': '63187916e336480b6f8aed82', 'port': 3503},
	{'profile_id': '63187a1e88e2ee2e6fcd1165', 'port': 3504},
	{'profile_id': '63187ab57addf177e54cb465', 'port': 3505},
	{'profile_id': '6318d07867ebfd6265cc2b14', 'port': 3506},

	]

if __name__ == '__main__':
	freeze_support()
	with Pool(8) as p:
		p.map(scrap, profiles)


	if platform == "win32":
		os.system('taskkill /im chrome.exe /f')
		os.system('taskkill /im chromedriver.exe /f')
	else:
		os.system('killall -9 chrome')
		os.system('killall -9 chromedriver')
