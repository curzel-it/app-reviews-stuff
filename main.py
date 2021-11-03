import argparse
import os
import json
from reviews import get_all_reviews

def get_and_store_reviews(app_id, args):  
  print('Getting: {0}'.format(app_id))
  reviews = get_all_reviews(app_id, args)
  data = { 'reviews': reviews }
  content = json.dumps(data, indent=4, sort_keys=True)
  
  filename = 'reviews-{0}.json'.format(app_id)
  path = os.path.join(args.destination, filename)
  f = open(path, 'w')
  f.write(content)
  f.close()

def run(args):
  for app_id in args.apps:
    get_and_store_reviews(app_id, args)


parser = argparse.ArgumentParser(
  description='Get App Store app reviews'
)
parser.add_argument(
  '--token', type=str, 
  help='Bearer Auth Token you got by inspecting the App Store website (just the token)'
)
parser.add_argument(
  '--apps', type=str, nargs="*",
  help='A list of App IDs, space separated'
)
parser.add_argument(
  '--platforms', type=str, nargs="*",
  help='List of platforms (iphone, ipad, mac, appletv), space separated'
)
parser.add_argument(
  '--locale', type=str, 
  help='Locale in the usual format, it-IT, en-US, ...'
)
parser.add_argument(
  '--max-reviews', type=int, nargs='?', default=100,
  help='Max number of reviews to fetch for each app'
)
parser.add_argument(
  '--take-it-easy', action='store_true',
  help='Uses longer delays between requests to avoid rate limit'
)
parser.add_argument(
  '--destination', type=str, nargs='?', default='.',
  help='Destination folder'
)
args = parser.parse_args()

os.system('mkdir -p {0}'.format(args.destination))
run(args)