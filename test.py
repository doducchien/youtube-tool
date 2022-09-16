import profile
from pygologin.gologin import GoLogin


gl = GoLogin({
    'token': '123',
    'profile_id': '631fe180c928671c3a8b5304',
    'spawn_browser':True
})
dba = gl.start()

print('dba', dba)