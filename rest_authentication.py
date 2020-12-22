import requests
import json
from jsonpath import jsonpath
#Ideally it works by passing username and password in auth= keyword argument but for github API it works via token
res = requests.get(
    url= 'https://api.github.com/user',
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token 0ea6446be101cafe2b69cab9d8b54ed23e71c951'},
    verify = False
)

print(res.status_code)
print(res.text)