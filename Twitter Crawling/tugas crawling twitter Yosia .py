# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:54:16 2019

@author: YOSIA AZARYA
"""

import tweepy
from tweepy import OAuthHandler

consumer_key = 'I46Q7ivTc1RUyvELwa9Cq5Ve2'
consumer_secret = '5KDKxtknmaUjaxkz1bCwL2DpHqSb3sAOFKSHWmbhxdPlQfv9WF'
access_token = '40819539-KteoSEoTObWF2D202ud8wDbnnxa1uIV1Hs05EInBg'
access_secret = 'DhyaJl0LC7BC9RJ0m1WIP3k6x1tEV8FNDrGxA88XpJ5T1'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

target = ['karniilyas', 'mohmahfudmd', 'detikcom', 'kompascom', 'korantempo']

for siapapun in target:
    user = api.get_user(id=siapapun)
    
    with open(siapapun+'_tweets.txt', 'w') as myfile:
        myfile.write("Info \n")
        myfile.write("\n")
        myfile.write("Account : " + siapapun + "\n")
        myfile.write("\n")
        myfile.write("Name : " + user.name + "\n")
        myfile.write("\n")
        myfile.write("Screen Name : " + user.screen_name + "\n")
        myfile.write("\n")
        myfile.write("Description : " + user.description + "\n")
        myfile.write("\n")
        myfile.write("Followers count : " + str (user.followers_count) + "\n")
        myfile.write("\n")
        myfile.write("Last 20 Tweets")
        myfile.write("\n")
        
        for status in tweepy.Cursor(api.user_timeline, id=siapapun).items(20):
        
            myfile.write(status.text + "\n")
            myfile.write("\n")

            
            
        
    