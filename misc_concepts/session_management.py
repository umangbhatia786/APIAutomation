import requests
import json
from jsonpath import jsonpath

se = requests.session()
se.headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token dfbfea7d59dd84cf4a156d36aefe2d4ab27b2464', 'User-Agent': 'github'},
user_res = se.get(
    url= 'https://api.github.com/user',
)

print(user_res.status_code)
print(user_res.text)

repo_res = se.get(
    url= 'https://api.github.com/user/repos'
)

print(repo_res.status_code)
print(repo_res.text)

