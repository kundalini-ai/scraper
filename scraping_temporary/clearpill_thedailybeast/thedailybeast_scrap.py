import requests
import multiprocessing
from functools import partial

s = requests.Session()

cookies = {
    'AKA_A2': 'A',
    'ak_bmsc': '7559E88C6916D1545E17DD1AF642FF8F~000000000000000000000000000000~YAAQVvvhuamxU2KQAQAAc1u/nRiLWxYuZuAbx27IgySVNJsrk4Bect486BSV4uDblqwdFfJsjhBQY7/EM1fc7EdaQAGmftTB0xnpKB2A0dmzLQo94ir9r0vMoRD5dJXQG1Q1DH/V96+M82JoycW30sVlA2rsnBroGXAqo28xh7RM5VA1PH/33ZLIeL7jzEAMzsEqW9o58J4MmC+KOlrHmAix6faaCs6plVLn5IBO4P8L8NTuKfEnztda4SMfb7rvfZz9aStSyqpLZOF+FNeE87Sj+NvRqi1P5a2gK9WYb8FhtlRXTsUYMprmaK580aiT1mQHDymxeqVyhgSk5Gdp6mulIRu6+fPM8f/xVRzA4EXeayuaOeskyjLdcvQTEwXu/UrEMwiPSFsPdb3M8yjocm6Y+g==',
    'usprivacy': '1---',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAdgBZuHAJy8ATAAZeAVknDh-AGwgAvkA',
    '_pcid': '%7B%22browserId%22%3A%22lyg4qzyxhxt80m6w%22%7D',
    '__pat': '-14400000',
    '_pcus': 'eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHM6MjBlNGU3YzViYjBmZmVhNTNhZTFlYTUwYTA1ZjZiNWZkMWZkMzI1Zjpub19zY29yZSIsIkxUYzpmMTFjZDViNTMzODEyOWI0NDkyNmZmOGQzNDg3ZDQxYWExMTVlNTg2Om5vX3Njb3JlIiwiTFRyZWc6ZDQ1ZGI2NWQ0MjkyMDljYzVmNmYxNjY4YmFhN2ZjMGEwZGUxMjRhMzpub19zY29yZSIsIkxUcmV0dXJuOjg2ODBhZGYyMmNhOTljMjg4ZDliNDEyOTAwZDA1MTE1ODhhNWNlODc6bm9fc2NvcmUiLCJDU2NvcmU6MDc2YzA3MGQ1N2ZmZmMyZWQ5YjY2ZmIyMjRhMWY4OGQyMWEyMGUwZTpub19zY29yZSJdfX19',
    '__pid': '.thedailybeast.com',
    'OneTrustWPCCPAGoogleOptOut': 'true',
    '_pc_annoyed': '1',
    '_pc_hp': '1',
    '__pil': 'en_US',
    'OptanonAlertBoxClosed': '2024-07-10T17:48:30.074Z',
    'eupubconsent-v2': 'CQBiPzAQBiPzAAcABBENA7E8AP_gAEPgACiQKTgBoCBEAQBJIGBiAIIAAAAEQBhAQAAAAAAAAAAABAAABAAAAAAAAAAAEAAAAAIAAAAAAAJAABAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIgAAAAAAAAAAAAgAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAACAAAAAAAADF_rE2_eT1l_tevp7D9-cts7_XW-9_fff79Ll_-mB_gpKAGAIEQAAEAAQEAAAAAAAABAEABAAAAAAAAAAAAEAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAQAAAAAAAAAAAAAAAAiAAAAAAAAAAAACAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIg2gAAIAEAggAqEUnZgCCAM2WqvFk2jK0gLR8wXvaYAAA.f_wACHwAAAAA',
    '__tdbbrowser': 'aeca5250-eaf5-4ac4-a246-0171a842e322',
    '__tdbbrowser.sig': 'pTVthADOLMyuViaZBPfvUGnnm24',
    '__tdbsesh': 'eyJub3dJbk1pbnV0ZXMiOjI4Njc3MjI5LCJzZXNzaW9uSWQiOiIxYTAyN2FiYS0xY2Y1LTRhNmItODA3MC1lOTQ1Yzc3ZmEwNWMiLCJkZnBCdWNrZXRJZCI6MTN9',
    '__tdbsesh.sig': 'UDFfnG2GTFdH5BN8Q023hUbYLa0',
    'bm_mi': '1F6707F1F199BC233979B4CD9E32DD0B~YAAQHfvhuTa3BpuQAQAA99LDnRgjLMZl3uJ4+WtZsNn7+NSG9vPmvbVgjHCi5kf6DVoj0v+y2eyR7c/atK5uxucGOm776WPuQbxg292VaoD7+KmGRGH1/jHfhU6tepn4RO3yYYfvlmpfonCn/vipDYz4efTSkonFdr9rmJaVo6v1dmsbPwXF6+Y/KrDYoTy3qicbZpJfjp4uXkIcykBo/3jd6jeGjthm+YkQFZnR6UHQvqEYawIkmfNrlnKc9GfzkcAWA2nIF5351x9Z5RmUdLh2dysgK2IdiK1/umgkgnTBIjTlFmT+ZaAffJb2D96minLa8UZC3sZpJ+Y+pHBwHUFADQ==~1',
    'bm_sv': '522E0F4C2B1A64001FE9E4638D152A65~YAAQHfvhuTe3BpuQAQAA99LDnRiAxSjeHw9m3+/Cs5/Yf6xLMigkXp3vOWX1fIqyEjyBCwz2/EZrFvfR+CgXujSKXGFmkYDWCG/Rp4NNjPAhqDvU7IojszsXeMCpta1wL7skXO/nHe51lx43zcbsM7ZaCEUHgG3CtDc8dBqxzMC/SjATbjWpso0+gpVgaXfFuBxmH2QstJcRK27Q8mh2P0HvMTxiGm3z739SEydHH1kMwyBjEpPsi1QPFDMZzAkHWlxUPULIFA==~1',
    '__tdb24': '1',
    'audience_segment': 'referral',
    'audience_segment_source': 'www.thedailybeast.com',
    '__pvi': 'eyJpZCI6InYtbHlnNHF6ejM0ZmpxNTBmNyIsImRvbWFpbiI6Ii50aGVkYWlseWJlYXN0LmNvbSIsInRpbWUiOjE3MjA2MzM3NzUzNTl9',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Jul+10+2024+19%3A49%3A35+GMT%2B0200+(Central+European+Summer+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0a4dfa19-0070-49f6-b4a5-f4a5c9d3346e&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CBG32%3A1%2CV2STACK42%3A1&AwaitingReconsent=false&intType=1&geolocation=PL%3B24',
    '__tbc': '%7Bkpex%7DTILcQAj3XfE_7FOQ1w17V0OiLyGMt8IcTbF-3BqEjVucgKBKbGGnjiZ-QCrc8XKn',
    'xbc': '%7Bkpex%7DfIHYQMAWD-k2Y-glWiYMT2-qh2R7xjNNOYmCXraczHbIUmFQKWvOZNEM6F9_W5aq8Ql0nAoWJoNqMAIWESm3hgvaMQJgGYSA_kR207zSsE0',
}

headers = {
    'authority': 'www.thedailybeast.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
    # 'cookie': 'AKA_A2=A; ak_bmsc=7559E88C6916D1545E17DD1AF642FF8F~000000000000000000000000000000~YAAQVvvhuamxU2KQAQAAc1u/nRiLWxYuZuAbx27IgySVNJsrk4Bect486BSV4uDblqwdFfJsjhBQY7/EM1fc7EdaQAGmftTB0xnpKB2A0dmzLQo94ir9r0vMoRD5dJXQG1Q1DH/V96+M82JoycW30sVlA2rsnBroGXAqo28xh7RM5VA1PH/33ZLIeL7jzEAMzsEqW9o58J4MmC+KOlrHmAix6faaCs6plVLn5IBO4P8L8NTuKfEnztda4SMfb7rvfZz9aStSyqpLZOF+FNeE87Sj+NvRqi1P5a2gK9WYb8FhtlRXTsUYMprmaK580aiT1mQHDymxeqVyhgSk5Gdp6mulIRu6+fPM8f/xVRzA4EXeayuaOeskyjLdcvQTEwXu/UrEMwiPSFsPdb3M8yjocm6Y+g==; usprivacy=1---; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAdgBZuHAJy8ATAAZeAVknDh-AGwgAvkA; _pcid=%7B%22browserId%22%3A%22lyg4qzyxhxt80m6w%22%7D; __pat=-14400000; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHM6MjBlNGU3YzViYjBmZmVhNTNhZTFlYTUwYTA1ZjZiNWZkMWZkMzI1Zjpub19zY29yZSIsIkxUYzpmMTFjZDViNTMzODEyOWI0NDkyNmZmOGQzNDg3ZDQxYWExMTVlNTg2Om5vX3Njb3JlIiwiTFRyZWc6ZDQ1ZGI2NWQ0MjkyMDljYzVmNmYxNjY4YmFhN2ZjMGEwZGUxMjRhMzpub19zY29yZSIsIkxUcmV0dXJuOjg2ODBhZGYyMmNhOTljMjg4ZDliNDEyOTAwZDA1MTE1ODhhNWNlODc6bm9fc2NvcmUiLCJDU2NvcmU6MDc2YzA3MGQ1N2ZmZmMyZWQ5YjY2ZmIyMjRhMWY4OGQyMWEyMGUwZTpub19zY29yZSJdfX19; __pid=.thedailybeast.com; OneTrustWPCCPAGoogleOptOut=true; _pc_annoyed=1; _pc_hp=1; __pil=en_US; OptanonAlertBoxClosed=2024-07-10T17:48:30.074Z; eupubconsent-v2=CQBiPzAQBiPzAAcABBENA7E8AP_gAEPgACiQKTgBoCBEAQBJIGBiAIIAAAAEQBhAQAAAAAAAAAAABAAABAAAAAAAAAAAEAAAAAIAAAAAAAJAABAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIgAAAAAAAAAAAAgAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAACAAAAAAAADF_rE2_eT1l_tevp7D9-cts7_XW-9_fff79Ll_-mB_gpKAGAIEQAAEAAQEAAAAAAAABAEABAAAAAAAAAAAAEAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAQAAAAAAAAAAAAAAAAiAAAAAAAAAAAACAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIg2gAAIAEAggAqEUnZgCCAM2WqvFk2jK0gLR8wXvaYAAA.f_wACHwAAAAA; __tdbbrowser=aeca5250-eaf5-4ac4-a246-0171a842e322; __tdbbrowser.sig=pTVthADOLMyuViaZBPfvUGnnm24; __tdbsesh=eyJub3dJbk1pbnV0ZXMiOjI4Njc3MjI5LCJzZXNzaW9uSWQiOiIxYTAyN2FiYS0xY2Y1LTRhNmItODA3MC1lOTQ1Yzc3ZmEwNWMiLCJkZnBCdWNrZXRJZCI6MTN9; __tdbsesh.sig=UDFfnG2GTFdH5BN8Q023hUbYLa0; bm_mi=1F6707F1F199BC233979B4CD9E32DD0B~YAAQHfvhuTa3BpuQAQAA99LDnRgjLMZl3uJ4+WtZsNn7+NSG9vPmvbVgjHCi5kf6DVoj0v+y2eyR7c/atK5uxucGOm776WPuQbxg292VaoD7+KmGRGH1/jHfhU6tepn4RO3yYYfvlmpfonCn/vipDYz4efTSkonFdr9rmJaVo6v1dmsbPwXF6+Y/KrDYoTy3qicbZpJfjp4uXkIcykBo/3jd6jeGjthm+YkQFZnR6UHQvqEYawIkmfNrlnKc9GfzkcAWA2nIF5351x9Z5RmUdLh2dysgK2IdiK1/umgkgnTBIjTlFmT+ZaAffJb2D96minLa8UZC3sZpJ+Y+pHBwHUFADQ==~1; bm_sv=522E0F4C2B1A64001FE9E4638D152A65~YAAQHfvhuTe3BpuQAQAA99LDnRiAxSjeHw9m3+/Cs5/Yf6xLMigkXp3vOWX1fIqyEjyBCwz2/EZrFvfR+CgXujSKXGFmkYDWCG/Rp4NNjPAhqDvU7IojszsXeMCpta1wL7skXO/nHe51lx43zcbsM7ZaCEUHgG3CtDc8dBqxzMC/SjATbjWpso0+gpVgaXfFuBxmH2QstJcRK27Q8mh2P0HvMTxiGm3z739SEydHH1kMwyBjEpPsi1QPFDMZzAkHWlxUPULIFA==~1; __tdb24=1; audience_segment=referral; audience_segment_source=www.thedailybeast.com; __pvi=eyJpZCI6InYtbHlnNHF6ejM0ZmpxNTBmNyIsImRvbWFpbiI6Ii50aGVkYWlseWJlYXN0LmNvbSIsInRpbWUiOjE3MjA2MzM3NzUzNTl9; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jul+10+2024+19%3A49%3A35+GMT%2B0200+(Central+European+Summer+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0a4dfa19-0070-49f6-b4a5-f4a5c9d3346e&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CBG32%3A1%2CV2STACK42%3A1&AwaitingReconsent=false&intType=1&geolocation=PL%3B24; __tbc=%7Bkpex%7DTILcQAj3XfE_7FOQ1w17V0OiLyGMt8IcTbF-3BqEjVucgKBKbGGnjiZ-QCrc8XKn; xbc=%7Bkpex%7DfIHYQMAWD-k2Y-glWiYMT2-qh2R7xjNNOYmCXraczHbIUmFQKWvOZNEM6F9_W5aq8Ql0nAoWJoNqMAIWESm3hgvaMQJgGYSA_kR207zSsE0',
    'dnt': '1',
    'referer': 'https://www.thedailybeast.com/category/innovation',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

def scrap (url):
	r = s.get(url, headers=headers, cookies=cookies)
	if (r.status_code != 200):
		print(r.text)
		raise ValueError
	return r.text

def process_url(url):
	article_id = url[:-1].split('/')[-1]
	print('scraping article #{}'.format(article_id))
	content = scrap(url.rstrip())
	output_file = 'clearpill_thedailybeast_com/{}.html'.format(article_id)
	with open(output_file, 'w+') as output:
		output.write(content)

def main():
	print('[*] loading urls from clearpill_thedailybeast_links.txt')

	with open('clearpill_thedailybeast_links.txt', 'r') as f:
		urls = [url.strip() for url in f.readlines()]

	print('[*] {} loaded'.format(len(urls)))

	pool_size = multiprocessing.cpu_count() * 2
	with multiprocessing.Pool(pool_size) as pool:
		pool.map(process_url, urls)

if __name__ == '__main__':
	main()