from tinydb import Query, TinyDB
from requests import post
import argparse


db = TinyDB('db.json')
Form = Query()


def send_wrong_query(url='http://localhost:5000/get_form'):
    dct = {
        'email': 'test@asdczxczxc.ru',
        'phone': '%2B79995553322'
    }
    request = post(url, data=dct)
    if request.status_code == 200:
        print(request.json())


def send_correct_query(url='http://localhost:5000/get_form'):
    dct = {'name': 'test form 1',
           'phone': '+79991119999',
           'email': 'test@test.ru',
           'additional_field': 'vvv'}
    request = post(url, data=dct)
    if request.status_code == 200:
        print(request.json())


def test_queries():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', metavar='url', type=str, nargs='*')
    args = parser.parse_args()

    if 'url' in args and args.url:
        url = args.url[0]
        send_correct_query(url)
        send_wrong_query(url)
        return

    send_correct_query()
    send_wrong_query()


test_queries()