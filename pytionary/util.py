import requests
from bs4 import BeautifulSoup

def make_connection(type_name, word):
    re = requests.get(f'https://www.{type_name}.com/browse/{word}')
    if re.status_code != 200:
        print("There has been a connection error.Retrying....")
        make_connection(type_name, word)
    soup = BeautifulSoup(re.text, 'lxml')
    return soup
