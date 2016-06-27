#!/usr/bin/python
from flask import Flask
app = Flask(__name__)

import os

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    ckey = os.environ['TWITTER_CKEY']
    csecret = os.environ['TWITTER_CSECRET']
    atoken=os.environ['TWITTER_ATOKEN']
    asecret=os.environ['TWITTER_ASECRET']

    class listener(StreamListener):

        def on_data(self, data):
            print(data)
            return(True)

        def on_error(self, status):
            print status

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["devops"])    

    #app.run(host='0.0.0.0', port=5555)