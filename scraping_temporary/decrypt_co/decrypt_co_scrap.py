import requests
import multiprocessing
from functools import partial

cookies = {
	'CookieConsent': '{stamp:%2790JO7BhBpHmHHkUcCemQDrVxGN8k0PoP/5ZhaXQleOZ8edb1xOu0iA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1720467914289%2Cregion:%27pl%27}',
	'GDPR_Settings': '%7B%22doNotTrack%22%3Atrue%7D',
}

headers = {
	'authority': 'decrypt.co',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
	'cache-control': 'max-age=0',
	# 'cookie': 'CookieConsent={stamp:%2790JO7BhBpHmHHkUcCemQDrVxGN8k0PoP/5ZhaXQleOZ8edb1xOu0iA==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1720467914289%2Cregion:%27pl%27}; GDPR_Settings=%7B%22doNotTrack%22%3Atrue%7D',
	'dnt': '1',
	'if-none-match': '"6xqvn2jvl4fuia"',
	'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Linux"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

s = requests.Session()

def scrap (url):
	r = s.get(url, cookies=cookies, headers=headers)
	if (r.status_code != 200):
		print(r.text)
		raise ValueError
	return r.text

def process_url(url):
	article_id = url[:-1].split('/')[-2]
	print('scraping article #{}'.format(article_id))
	content = scrap(url.rstrip())
	output_file = 'decrypt_co/{}.html'.format(article_id)
	with open(output_file, 'w+') as output:
		output.write(content)

def main():
	print('[*] loading urls from decrypt_co_urls.txt')

	with open('decrypt_co_urls.txt', 'r') as f:
		urls = [url.strip() for url in f.readlines()]

	print('[*] {} loaded'.format(len(urls)))

	pool_size = multiprocessing.cpu_count() * 2
	with multiprocessing.Pool(pool_size) as pool:
		pool.map(process_url, urls)

if __name__ == '__main__':
	main()