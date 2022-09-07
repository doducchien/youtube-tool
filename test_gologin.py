from pygologin.gologin import GoLogin

gl = GoLogin({
    'token': '1eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzE4Nzg0ZjYyY2RiZDZlYTQzNTZmOGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzE4OGNjMWUzNGIwODIyMGE2ZWRjOWIifQ.whKBz_jbenkPCj_Hw5Wdqybgc7PTn_SOnkSOK9l_kag',
    'profile_id': '63187ab57addf177e54cb465'
})



# print(type(gl))
debugger_address  = gl.start()

for property in [a for a in dir(debugger_address) if not a.startswith('__')]:
    print("{}: {}".format(gl, getattr(gl, property)))