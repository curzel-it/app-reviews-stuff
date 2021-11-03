# App Reviews Stuff
Python scripts I quickly put together to get app reviews from App Store.

## Usage
```
usage: main.py [-h] [--token TOKEN] [--apps [APPS ...]] [--platforms [PLATFORMS ...]] [--locale LOCALE] [--max-reviews [MAX_REVIEWS]] [--take-it-easy] [--destination [DESTINATION]]

Get App Store app reviews

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         Bearer Auth Token you got by inspecting the App Store website
  --apps [APPS ...]     A list of App IDs, space separated
  --platforms [PLATFORMS ...]
                        List of platforms (iphone, ipad, mac, appletv), space separated
  --locale LOCALE       Locale in the usual format, it-IT, en-US, ...
  --max-reviews [MAX_REVIEWS]
                        Max number of reviews to fetch for each app
  --take-it-easy        Uses longer delays between requests to avoid rate limit
  --destination [DESTINATION]
                        Destination folder
```
Example, getting 100 reviews for instagram:
```
python3 main.py \
  --apps 389801252 \
  --platforms iphone ipad \
  --locale en-US \
  --token <token> \
  --take-it-easy \
  --max-reviews 100
```

## Where do I get the auth token?
1. On your browser go to the App Store page for any app
1. Find the reviews section and tap "See All", [should look like this](https://apps.apple.com/us/app/instagram/id389801252#see-all/reviews)
1. Open up the Dev Tools, go to network and filter requests by `reviews?`
1. From any request, copy the Bearer token from the Authorization header (just the token)