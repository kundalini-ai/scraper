import requests, json

cookies = {
    'cf_clearance': 'HFIFM.iU1bHVbhLzFlcS1QALKBkKs7gLezaytr_aqs8-1720457818-1.0.1.1-6EcH27dAn9yjPN6WFEdasRj7.S_Hz9VXPTdm.8uQtgaHOFdYUfBRtGiMI_kFXVmr8rgBCSX_jsDHEtGmGnv3rQ',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Jul+08+2024+17%3A30%3A41+GMT%2B0200+(Central+European+Summer+Time)&version=202301.2.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.theblock.co%2F&groups=C0001%3A1%2CC0002%3A0%2CSTACK42%3A0',
    'new-free-nl-exists': 'true',
    'free-newsletter-count': '5',
    'email-modal-suppress-dismiss': '1',
    '__cf_bm': '31fvKeQxqfExUhLjLm7tSh57HW3k1Mj.U_VJcjl_N5I-1720457807-1.0.1.1-ds3.G4aAy0Z0dK1494yn8ks4plVhW3y2YEf__xdXZw_styV9Ky5LN8CkucpaQiZ_7F9uV8_xOGq6bbviIEbDLw',
}

headers = {
    'authority': 'www.theblock.co',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
    # 'cookie': 'cf_clearance=z8gnGCuuIO0JBubDac3oqM4tSPGNPf_kPZAVlpg1dtU-1720452641-1.0.1.1-qUer5NYbQtTcZxw72s9husNGG8mFjizCIePLlnDdxlVHmideWSDKY4B9kEtojROQqgzlHgsrz2QSvEM12Lv4Gw; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jul+08+2024+17%3A30%3A41+GMT%2B0200+(Central+European+Summer+Time)&version=202301.2.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.theblock.co%2F&groups=C0001%3A1%2CC0002%3A0%2CSTACK42%3A0; new-free-nl-exists=true; free-newsletter-count=5; email-modal-suppress-dismiss=1; __cf_bm=bRCkwhLx.ni2N5.wdX5N6vxC.tJQ3j9KASsFHWGzA98-1720456051-1.0.1.1-c0ocOAuCFaea3c1wXkL6PFfDoANABWgPvUQyBJQzJX3colEX5Z69y_LrNiOiATuNGvFJhjjC_esMYkzrJuFv6A',
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

def fetch_batch (start=0, recursion_depth=0):
	if (recursion_depth > 40):
		print('reached 40 recursion depth in fetch_batch at article offset {}'.format(start))
		return []

	size = 1000-recursion_depth

	r = requests.get(
    'https://www.theblock.co/api/search?query=matchall&selectedDifficulties=&selectedFilterCategories=&slug=&size={}&start={}&return=cid,authors,title,url,label,thumbnail,publishedFormatted,primaryCategory,difficulty,body'.format(size, start),
    	cookies=cookies,
    	headers=headers,
	)

	data = r.json()

	if 'error' in data:
		if 'error' == "Class WP_Post not found in given scope": # we're trying to start from an article that doesn't exist, let's bump it up a notch
			return fetch_batch(start+1, recursion_depth+1)

	try:
		return r.json()['articles']
	except KeyError:
		print(r.text)
		return []

def process_articles (articles):
	for article in articles:
		with open('theblock_co/{}.json'.format(article['id']), 'w+') as f:
			f.write(json.dumps(article))

for x in range(10, 23):
	articles = fetch_batch(x*1000)
	print('fetched {} articles, processing'.format(len(articles)))
	process_articles(articles)