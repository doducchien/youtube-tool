from multiprocessing import freeze_support
from pygologin.gologin import GoLogin
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
gl = GoLogin({
    'token': '1eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzE4Nzg0ZjYyY2RiZDZlYTQzNTZmOGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzE4OGNjMWUzNGIwODIyMGE2ZWRjOWIifQ.whKBz_jbenkPCj_Hw5Wdqybgc7PTn_SOnkSOK9l_kag',
    'profile_id': '63187ab57addf177e54cb465'
})



# print(type(gl))
debugger_address  = gl.start()
print("debugger_address:", debugger_address)

# for property in [a for a in dir(debugger_address) if not a.startswith('__')]:
#     print("{}: {}".format(gl, getattr(gl, property)))
# gl.stop()


# if __name__ == "__main__":
#     print(debugger_address)




if __name__ == '__main__':
    freeze_support()
    options = Options()
    options.add_experimental_option('debuggerAddress', debugger_address)
    time.sleep(5)
    driver = Chrome(executable_path='chromedriver.exe', options=options)
    # driver = webdriver.Remote(command_executor=debugger_address, options=webdriver.ChromeOptions())
    # driver.session_id = 'e08b404c-fd94-4aac-948f-adce63d6ed08'
    driver.get('https://youtube.com')
    time.sleep(10)
    driver.close()
    # gl.stop()
