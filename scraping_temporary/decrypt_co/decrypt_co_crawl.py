import requests, json

headers = {
    'authority': 'gateway.decrypt.co',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
    'apollo-require-preflight': 'true',
    'dnt': '1',
    'origin': 'https://decrypt.co',
    'referer': 'https://decrypt.co/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

def fetch_page_urls (page = 1):
    params = {
        'variables': json.dumps({
                'input': {
                    'perPage': 1000,
                    'topics': ['CRYPTO'],
                    'page': page
                }            
        }),
        'operationName': 'FeedPages',
        'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"44069b1a0ef7b6b0ea2792a6fc47b39bf3f544e645767a8fa6fffd7e6b3ad798"}}',
    }

    r = requests.get('https://gateway.decrypt.co/', params=params, headers=headers)
    data = r.json()

    urls = []
    for article in data['data']['feedPages']['result']:
        urls.append(article['url'])
    return urls
    
def main():
    print('[*] crawling urls to decrypt_co_urls.txt')

    with open('decrypt_co_urls.txt', 'w+') as f:
        for page in range(1,5): # todo this can be dynamically calculated from the response or "hasNextPage" param can be used
            print('[*] page {}'.format(page))
            for url in fetch_page_urls(page):
                if 'decrypt.co' in url:
                    f.write(url + '\n')

if __name__ == '__main__':
    main()