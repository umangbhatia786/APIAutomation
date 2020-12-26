import requests
from postPayload import *
from utilities.configuration import *
from utilities.resources import ApiResources


def after_scenario(context, scenario):
    context.delete_book_payload = requests.post(
        url=f'{context.my_config["API"]["endpoint"]}{ApiResources.delete_book}',
        json=delete_book_payload(context.book_id),
        headers={'Content-Type': 'application/json'}
    )
    assert context.delete_book_payload.status_code == 200, 'Book Deletion failed'
