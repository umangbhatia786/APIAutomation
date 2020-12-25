import requests
import json
from jsonpath import jsonpath
from postPayload import *
from utilities.configuration import *
from utilities.resources import ApiResources

my_query = 'Select * from Books'
config = get_config()
# Adding a book
add_book_res = requests.post(
    url=f'{config["API"]["endpoint"]}{ApiResources.add_book}',
    json=build_payload_from_db(my_query),
    headers={'Content-Type': 'application/json'}
)

print(add_book_res.status_code)
print(add_book_res.text)
res_json = add_book_res.json()
res_book_id = res_json['ID']

# Deleting a book

delete_book_payload = requests.post(
    url=f'{config["API"]["endpoint"]}{ApiResources.delete_book}',
    json=delete_book_payload(res_book_id),
    headers={'Content-Type': 'application/json'}
)

print(delete_book_payload.status_code)
