#!/usr/bin/env python

# made by @mrglennjones with help from @pimoroni & pb

import time
import unicodedata
try:
    import queue
except ImportError:
    import Queue as queue
from sys import exit

try:
    import tweepy
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip install tweepy")

from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font5x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

# adjust the tracked keyword below to your keyword or #hashtag
keyword = '#bilgetank'

# enter your twitter app keys here
# you can get these at apps.twitter.com
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

if consumer_key == '' or consumer_secret == '' or access_token == '' or access_token_secret == '':
    print("You need to configure your Twitter API keys! Edit this file for more information!")
    exit(0)

# make FIFO queue
q = queue.Queue()


# define main loop to fetch formatted tweet from queue
def mainloop():
    # Uncomment the below if your display is upside down
    #   (e.g. if you're using it in a Pimoroni Scroll Bot)
    # matrix11x7.rotate(degrees=180)
    matrix11x7.clear()
    matrix11x7.show()

    while True:
        # grab the tweet string from the queue
        try:
            matrix11x7.clear()
            status = q.get(False)
            matrix11x7.write_string(status, font=font5x7)
            status_length = matrix11x7.write_string(status, x=0, y=0, font=font5x7)
            time.sleep(0.25)

            while status_length > 0:
                matrix11x7.show()
                matrix11x7.scroll(1)
                status_length -= 1
                time.sleep(0.02)

            matrix11x7.clear()
            matrix11x7.show()
            time.sleep(0.25)

            q.task_done()

        except queue.Empty:
            time.sleep(1)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.text.startswith('RT'):
            # format the incoming tweet string
            status = u'     >>>>>     @{name}: {text}     '.format(name=status.user.screen_name.upper(), text=status.text.upper())
            try:
                status = unicodedata.normalize('NFKD', status).encode('ascii', 'ignore')
            except BaseException as e:
                print(e)

            # put tweet into the fifo queue
            q.put(status)

    def on_error(self, status_code):
        print("Error: {}".format(status_code))
        if status_code == 420:
            return False


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=[keyword], stall_warnings=True, async=True)


try:
    mainloop()

except KeyboardInterrupt:
    myStream.disconnect()
    del myStream
    print("Exiting!")
