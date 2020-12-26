from behave import given, when, then
from postPayload import *
from utilities.configuration import *
from utilities.resources import ApiResources
import requests


@given(u'The book details which need to be added to the library')
def step_impl(context):
    context.my_config = get_config()
    context.api_url = f'{context.my_config["API"]["endpoint"]}{ApiResources.add_book}'
    context.api_headers = {'Content-Type': 'application/json'}
    context.input_json = add_book_payload('MyPain', 'IUDTYC', 'Clark Kent')


@when(u'We execute the AddBook API method')
def step_impl(context):
    context.add_book_res = requests.post(
        url=context.api_url,
        json=context.input_json,
        headers=context.api_headers
    )


@then(u'Book is added successfully')
def step_impl(context):
    res_json = context.add_book_res.json()
    '''print(context.add_book_res.status_code)
    print(context.add_book_res.text)'''
    context.book_id = res_json['ID']
    assert context.add_book_res.status_code == 200, 'Status Code is not 200'
    assert res_json['Msg'] == 'successfully added', 'Add Book Message is not same as expected'
