import os
import gspread
from dotenv import load_dotenv
from scholarly import scholarly, ProxyGenerator
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv('config/.env')

SCRAPER_API_KEY = os.getenv('SCRAPER_API_KEY')
EMAIL_TO_SHARE = os.getenv('EMAIL_TO_SHARE')

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_key.json', scope)
client = gspread.authorize(creds)

sheet = client.create('iMotions Articles')

worksheet = sheet.get_worksheet(0)
worksheet.append_row(['Article Title',
                      'Author Names',
                      'Publication Year',
                      'Publication Link'])
                   

pg = ProxyGenerator()
pg.ScraperAPI(SCRAPER_API_KEY)
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs('"iMotions"', citations=True)
articles_data = []
# article_count = 0

while True:
    try:
        article = next(search_query)
        if 'bib' in article:
            article_title = article["bib"]["title"]
            authors = ", ".join(article["bib"]["author"])
            pub_year = article["bib"]["pub_year"]
            #pub_url = article["pub_url"]
            pub_url = article["pub_url"] if 'pub_url' in article else None
            
            
            
            articles_data.append([article_title, authors, pub_year, pub_url])
            # article_count += 1
            # print(f'\n{article_count}.')
            # print('Title: ', article_title)
            # print('Authors: ', authors)
            # print('Year: ', pub_year)
            # print('URL: ', pub_url)
    except StopIteration:
        break

worksheet.append_rows(articles_data)

sheet.share(EMAIL_TO_SHARE, perm_type='user', role='writer')