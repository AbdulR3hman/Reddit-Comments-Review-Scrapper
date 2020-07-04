from pprint import pprint

from google_play_scraper import Sort, reviews
import csv

result, continuation_token = reviews(
    'com.reddit.frontpage',
    lang='en',  # defaults to 'en'
    country='us',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    count=5000,  # defaults to 100
    # filter_score_with=5 # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.
# result, _ = reviews(
#     'com.reddit.frontpage',
#     continuation_token=continuation_token # defaults to None(load from the beginning)
# )
counter = 0

with open('reviews.csv', mode='w', newline='') as reviews_file:
    writer = csv.writer(reviews_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['content', 'score', 'thumbsUpCount'])
    for r in result:
        if r['content'].lower().find("comment") > -1:
            counter += 1
            try:
                writer.writerow([r['content'], r['score'], r['thumbsUpCount']])
            except:
                print("Caught exception")
            # print(r['content'], "," , r['score'], ",", r['thumbsUpCount'])

print("Number of reviews about comments:", counter)
