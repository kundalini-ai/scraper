import requests
from bs4 import BeautifulSoup

s = requests.Session()

headers = {
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://cryptonews.net/',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
}

def extract_links (content):
    links = []
    soup = BeautifulSoup(content, 'lxml')

    for anchor in soup.find_all('a', {'class': 'title'}):
        links.append('https://cryptonews.net' + anchor['href'])

    return links

def crawl_page (page=1):
    params = {
        'page': page,
        'axios': 'true',
    }

    r = s.get('https://cryptonews.net/', params=params, headers=headers)

    return extract_links(r.json()['html'])

with open('cryptonews_net_links.txt', 'w+') as f:
    page = 1
    while True:
        print('[*] page {}'.format(page))
        links = crawl_page(page)
        if (len(links) == 0):
            break
        for link in links:
            f.write(link + '\n')
        page += 1