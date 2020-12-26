from utilities.configuration import get_query


def add_book_payload(book_name, isbn, author):
    input_json = {
        "name": book_name,
        "isbn": isbn,
        "aisle": "227",
        "author": author
    }

    return input_json


def delete_book_payload(book_id):
    input_json = {
        "ID": book_id
    }

    return input_json


def build_payload_from_db(query):
    add_book = {}
    data_tuple = get_query(query)
    print(data_tuple)
    add_book['name'] = data_tuple[0]
    add_book['isbn'] = data_tuple[1]
    add_book['aisle'] = data_tuple[2]
    add_book['author'] = data_tuple[3]

    return add_book
