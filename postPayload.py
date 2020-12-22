def add_book_payload(book_name,isbn,author):
    input_json = {
        "name": book_name,
        "isbn": isbn,
        "aisle":"227",
        "author": author
        }

    return input_json

def delete_book_payload(book_id):
    input_json = {
        "ID" : book_id
        } 

    return input_json


