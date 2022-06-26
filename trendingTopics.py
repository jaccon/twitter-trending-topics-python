#!/usr/bin/env python
from twitter import *

import sys
sys.path.append(".")
import config

twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

results = twitter.trends.place(_id = 23424768)

print("UK Trends")

for location in results:
    for trend in location["trends"]:
        print(" - %s" % trend["name"])
