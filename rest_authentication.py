import requests
import json
from jsonpath import jsonpath
#Ideally it works by passing username and password in auth= keyword argument but for github API it works via token
res = requests.get(
    url= 'https://api.github.com/user',
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token dfbfea7d59dd84cf4a156d36aefe2d4ab27b2464'},
    verify = False
)

print(res.status_code)
print(res.headers)