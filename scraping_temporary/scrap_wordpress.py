import sys, requests, os, json

directory = sys.argv[1]
domain = sys.argv[2]

s = requests.Session()

headers = {
    'authority': 'thepointmag.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

def process_batch (articles):
	for article in articles:
		with open('{}/{}.json'.format(directory, article['id']), 'w+') as f:
			f.write(json.dumps(article))

def scrap_page (url, page=1, per_page=100):
	r = s.get('{}/wp-json/wp/v2/posts?_embed&per_page={}&page={}'.format(url, per_page, page), timeout=50, headers=headers)
	
	try:
		data = r.json()
	except requests.exceptions.JSONDecodeError as e:
		print(r.text)
		raise e

	if (r.status_code != 200):
		if (r.status_code == 400):
			if (data['code'] == 'rest_post_invalid_page_number'):
				return 0
	
	process_batch(data)

	return len(data)

# python3 scrap_wordpress.py directory, domain, start page
def main ():
	try:
		os.mkdir(directory)
	except FileExistsError:
		pass

	if (len(sys.argv) > 3):
		page = int(sys.argv[3])
	else:
		page = 1

	if (len(sys.argv) > 4):
		per_page = int(sys.argv[4])
	else:
		per_page = 100

	while True:
		print('[*] page {}'.format(page))
		articles_count = scrap_page(domain, page, per_page)
		if (articles_count == 0):
			break
		page += 1

	print('[*] done {}'.format(directory))

if __name__ == '__main__':
	main()