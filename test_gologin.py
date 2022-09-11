from lib2to3.pgen2 import driver
from multiprocessing import freeze_support
from pygologin.gologin import GoLogin

# gl = GoLogin({
#     'token': '1eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzE4Nzg0ZjYyY2RiZDZlYTQzNTZmOGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzE4OGNjMWUzNGIwODIyMGE2ZWRjOWIifQ.whKBz_jbenkPCj_Hw5Wdqybgc7PTn_SOnkSOK9l_kag',
#     'profile_id': '63187ab57addf177e54cb465'
# })



# print(type(gl))
# debugger_address  = gl.start()


# for property in [a for a in dir(debugger_address) if not a.startswith('__')]:
#     print("{}: {}".format(gl, getattr(gl, property)))
# gl.stop()


# if __name__ == "__main__":
#     print(debugger_address)



from undetected_chromedriver import Chrome, ChromeOptions;
from selenium.webdriver.common.by import By
if __name__ == '__main__':
    freeze_support()
    options = ChromeOptions()
    options.debugger_address = '127.0.0.1:26951'
    driver = Chrome(options=options)