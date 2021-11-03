import requests
import json
import time
import random

def get_reviews_page(auth_token, app_id, locale, platforms, offset=0, per_page=1):
  print('[{0}] Getting reviews, offset: {1}'.format(app_id, offset))
  url = 'https://amp-api.apps.apple.com/v1/catalog/us/apps/{0}/reviews?l={1}&offset={2}&platform=web&additionalPlatforms={3}&sparseLimit={4}'
  url = url.format(
    app_id.strip(), 
    locale, offset, 
    ','.join(platforms).replace(' ', ''), 
    per_page
  )
  response = requests.get(
    url, headers={'authorization': 'Bearer {0}'.format(auth_token)}
  )
  data = json.loads(response.content).get('data') or []
  return [d['attributes'] for d in data if _is_valid_review(d)]

def _is_valid_review(data):
  try:
    return data['attributes']['title'] != None
  except: return False

def get_all_reviews(app_id, args):
  print('[{0}] Getting all reviews...'.format(app_id))
  per_page = 50
  offset = 0
  reviews = []
  
  while True:
    new_reviews = get_reviews_page(
      args.token, 
      app_id, 
      args.locale, 
      args.platforms, 
      offset, per_page
    )
    offset += len(new_reviews)
    reviews += new_reviews
    if len(new_reviews) == 0: break
    if len(reviews) >= args.max_reviews: break
    delay = float(random.randint(100, 500)) / 1000
    time.sleep(delay)

  return reviews[:min(len(reviews), args.max_reviews)]