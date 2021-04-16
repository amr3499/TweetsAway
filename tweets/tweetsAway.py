# Alex Rosse
# CDT Red Team
# Python Script to send post requests to add potato pics
# to both blue team's web servers

import json
import requests
import time
import base64
import os

blue1url = 'http://10.0.1.4:5000/user/addtweet'
blue2url = 'http://10.0.2.4:5000/user/addtweet'

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

# Get Team 2 Users
blue2json = open('blue2.json',)
data2 = json.load(blue2json)
blue2json.close()
blue2 = []

for u in data2['following']:
    if (u['username']) not in redTeamUsers:
        blue2.append(u['id'])

# Loop through a folder of potato pics and encode them
potatoes = []
for filename in os.listdir('/home/alexandriarosse/Desktop/tweets/potatoez'):
    fullpath = os.path.join('/home/alexandriarosse/Desktop/tweets/potatoez/', filename)
    image = open(fullpath, 'rb')
    image_read = image.read()
    image_64 = base64.encodebytes(image_read)
    potatoes.append(image_64)

# Go until the user interrupts
#
# Loop through all blue1 and blue2 users sending a tweet of
# the next potato in the folder 
#
# Will wait 15 seconds after each request to not DoS the website,
# just be to annoying
while(1):
    counter = 0
    for u1 in blue1:
        req = {"userId" : (f"{u1}"), "text" : potatoes[counter % len(potatoes)]}
        res = requests.post(blue1url, json = req)
        print(res)
        counter += 1
        time.sleep(15)
    for u2 in blue2:
        req = {"userId" : (f"{u1}"), "text" : potatoes[counter % len(potatoes)]}
        res = requests.post(blue2url, json = req)
        print(res)
        counter += 1
        time.sleep(15)




