import requests

headers = {
    'authority': 'graphql-prod.thedailybeast.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.thedailybeast.com',
    'referer': 'https://www.thedailybeast.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

def process_links (links):
    with open('clearpill_thedailybeast_links.txt', 'a') as f:
        for link in links:
            f.write(link + '\n')

def fetch_batch (cursor):
    json_data = {
        'query': '{\n    vertical(slug: "innovation") {\n      stories(first: 100 after: "' + cursor + '" orderBy: { field: BUMP_DATE, direction: DESC }, shouldExcludeFromRecirculation: true) {\n        pageInfo {\n          hasNextPage\n        }\n        edges {\n          cursor\n          node {\n            vertical {\n              slug\n              name\n            }\n            ... on Article {\n              ...articleData\n            }\n            ... on Gallery {\n              ...galleryData\n            }\n          }\n        }\n      }\n    }\n\n    navigation {\n      id\n      name\n      path\n    }\n\n    screamer {\n      active\n      articleSlug: article_slug\n      bannerHeadline: banner_headline\n    }\n  }\n\n  fragment articleData on Article {\n    slug\n    canonicalSlug: canonical_slug\n    audience\n    rubric\n    shortHeadline: short_headline\n    description\n    publicationDate: publication_date\n    socialHeadline: social_headline\n    rights\n    Campaign: campaign {\n      ...campaignData\n    }\n    Metadata: metadata {\n      ...metadataData\n    }\n    Images: images {\n      public_id\n      version\n      url\n      title\n      rights\n      main_image\n      alt_text\n      crops\n    }\n    Authors: authors {\n      name\n      email\n      slug\n    }\n  }\n\n  fragment galleryData on Gallery {\n    slug\n    canonicalSlug: canonical_slug\n    rubric\n    shortHeadline: short_headline\n    description\n    publicationDate: publication_date\n    socialHeadline: social_headline\n    rights\n    Campaign: campaign {\n      ...campaignData\n    }\n    Metadata: metadata {\n      ...metadataData\n    }\n    Images: images {\n      public_id\n      version\n      url\n      title\n      rights\n      main_image\n      alt_text\n      crops\n    }\n    Authors: authors {\n      name\n      email\n      slug\n    }\n  }\n  fragment metadataData on Metadata {\n  sponsored\n  branded\n  specialContentFlag: special_content_flag\n  explicit\n  tragedy\n  no_crawl\n  violence\n  product_name\n}\n  fragment campaignData on Campaign {\n    id\n    name\n    slug\n    description\n    Brand: brand {\n      name\n      slug\n    }\n  }\n',
    }

    r = requests.post('https://graphql-prod.thedailybeast.com/graphql', headers=headers, json=json_data)

    links = []

    data = r.json()
    cursor = data['data']['vertical']['stories']['edges'][-1]['cursor']
    for story in data['data']['vertical']['stories']['edges']:
        links.append('https://www.thedailybeast.com/' + story['node']['slug'])

    process_links(links)
    return cursor

cursor = 'eyJ2IjoxLCJ2YWwiOiIyMDI0LTA0LTAxVDA4OjE5OjQyLjQwNloiLCJjIjoiYzYifQ=='
while True:
    cursor = fetch_batch(cursor)