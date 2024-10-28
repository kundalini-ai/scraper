import requests
import multiprocessing
from functools import partial

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

def scrap (url):
	r = s.get(url, headers=headers)
	if (r.status_code != 200):
		print(r.text)
		raise ValueError
	return r.text

def process_url(url):
	article_id = url[:-1].split('/')[-1]
	print('scraping article #{}'.format(article_id))
	content = scrap(url.rstrip())
	output_file = 'cryptonews_net/{}.html'.format(article_id)
	with open(output_file, 'w+') as output:
		output.write(content)

def main():
	print('[*] loading urls from cryptonews_net_urls.txt')

	with open('cryptonews_net_urls.txt', 'r') as f:
		urls = [url.strip() for url in f.readlines()]

	print('[*] {} loaded'.format(len(urls)))

	pool_size = multiprocessing.cpu_count() * 2
	with multiprocessing.Pool(pool_size) as pool:
		pool.map(process_url, urls)

if __name__ == '__main__':
	main()