from pprint import pprint

from google_play_scraper import app

result = app(
    'com.reddit.frontpage',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

pprint(result)