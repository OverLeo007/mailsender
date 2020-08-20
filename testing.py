import requests
import random as ran
import urllib.parse
import string as s

uencode = urllib.parse.quote
syms = ''.join(list(s.printable)[:-38])
rjson = dict()
rjson['from'] = input('from\n')
rjson['to'] = input('to\n')
rjson['subject'] = ''.join([ran.choice(syms) for _ in range(ran.randint(5, 20))])
rjson['body'] = ''.join([ran.choice(syms) for _ in range(ran.randint(20, 200))])
url = urllib.parse.urlencode(rjson)
print(url)
r = requests.post('http://mailspoofer.herokuapp.com/',
                  url)
print(r.status_code)