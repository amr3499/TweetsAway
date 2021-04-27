import json
import requests
import sys

#Arg 1 = Tweet ID
tweetId = str(sys.argv[1])
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiZjg4ODNiMGMtNThhNy00MTg3LThmNTItYjE2NjYyMWViNGI4In0sImlhdCI6MTYxODUyNDY2OX0.Csfgfcr54rKSA2D_ktFmkXgPbrK9SjjCA05dc6SnQ5k'

url = 'http://10.0.1.4:5000/tweet/remove'
headers = {"Authorization": "Bearer %s" % token}
req = {"tweetId":(f"{tweetId}")}

res = requests.delete(url, json = req, headers=headers)
print(res)
