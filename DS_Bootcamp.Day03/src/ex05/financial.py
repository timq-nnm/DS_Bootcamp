import httpx
import sys
from bs4 import BeautifulSoup
from lxml import etree
import time

def get_args(argv):
    if len(argv) < 2 or len(argv[1]) != 4:
        raise Exception('Invalid ticker')
    return argv[1], argv[2]


def check_response(url):
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    }
    
    response = httpx.get(url, headers=headers)

    if response.status_code == 302:
        raise Exception('Invalid ticker')
    elif response.status_code != 200:
        raise Exception(f'Connection error. Status code: {response.status_code}')
    
    return response


def get_response():
    ticker, metric = get_args(sys.argv)
    
    url = f'https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker}'
    response = check_response(url)

    soup = BeautifulSoup(response.text, "lxml")
    dom = etree.HTML(str(soup))

    body = soup.body
    h1_tags = soup.find_all('h1')

    xpath_str = f'//div[@title="{metric}"]/../../div[contains(@class,"column")]'

    result = list({metric})

    for element in dom.xpath(xpath_str):
        if element.text is not None and element.text.strip() != '':
            result.append(element.text.strip())

    if len(result) == 1:
        raise Exception('Invalid metric')

    result = tuple(result)
    print(result)


if __name__ == '__main__':
    time.sleep(5)
    get_response()