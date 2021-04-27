import json
import requests
import sys

tweetId = str(sys.argv[1])
token = ''

url = 'http://10.0.2.4:5000/tweet/remove'
headers = {"Authorization": "Bearer %s" % token}
req = {"tweetId":(f"{tweetId}")}

res = requests.delete(url, json = req, headers=headers)
print(res)
