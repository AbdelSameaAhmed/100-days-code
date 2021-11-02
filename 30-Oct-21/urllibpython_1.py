# ----------------
# urllib ---------
# ----------------

import urllib.request, urllib.response
# try:
#     x = urllib.request.urlopen('http://www.googlr.com/search?q=test')
#     print(x.read())
# except Exception as e:
#     print(str(e))
# reult of above code is "HTTP Error 404: Not Found"

try:
    url = 'http://www.googlr.com/search?q=test'
    headers = {}
    headers['User-Agent'] = 'Chrome/'
    req = urllib.request.Request( url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))