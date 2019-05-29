from datetime import datetime
import logging
import requests

import tweepy

from secrets import A_TOKEN, A_TOKEN_SECRET, C_KEY, C_SECRET

logging.basicConfig(
    filename='sun_will_rise.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('Starting sun_will_rise_script')

# Tweepy auth
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

# Get sunrise info from sunrise-sunset.org
params = {
    'lat': -33.900387,
    'lng': 18.413332,
}
sunrise_response = requests.get('https://api.sunrise-sunset.org/json', params=params).json()
did_sunrise = sunrise_response.get('results').get('sunrise') is not None

# Get today's date
today = datetime.today().strftime('%d %b %Y')

# Construct tweet
did_sunrise_str = 'Yes' if did_sunrise else 'No'
did_sunrise_tweet = f'{today}: {did_sunrise_str}'

api.update_status(did_sunrise_tweet)

logger.info(f'Tweeted: {did_sunrise_tweet}')


