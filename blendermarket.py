import bs4
from bs4 import BeautifulSoup
import requests
from itertools import chain
import cookies


def checkLoggedIn():
    return True

def getPurchases():
    orders = listOrders()
    items = [getPurchasesFromOrder(url) for url in orders]
    return chain.from_iterable(items)


def listOrders() -> [str]:
    body = fetch('https://blendermarket.com/account/orders')

    orders = [x.parent.get('href') for x in body.select("td > a > i.fa-download")]
    return orders

def getPurchasesFromOrder(url: str) -> (str, [(str, str)]):
    body = fetch(url)

    rows = body.select('div.card-body.row')
    for row in rows:
        name = [x.text for x in row.select('div:nth-child(1) a:nth-child(2)')][0]
        files = [(x.text, 'https://blendermarket.com' + x.get('href')) for x in row.select('div:nth-child(2) li>a')]

        yield (name, files)

def fetch(url: str) -> bs4.BeautifulSoup:
    r = requests.get(url, cookies=cookies.cookies)
    if r.status_code != 200:
        return None

    body = BeautifulSoup(r.text)
    if not checkLoggedIn():
        return None

    return body
