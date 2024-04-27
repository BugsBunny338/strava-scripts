import sys
import requests
from requests_oauthlib import OAuth2Session
import json

#####
# STEP 0
# Create an app to obtain client_id and client_secret
# https://www.strava.com/settings/api
client_id = ''
client_secret = ''
#####


#####
# STEP 1
# OAuth Authorization
# Run the code below to obtain authorization link
# Open authorization link in your browser and click authorize
# When redirected, copy the 'code' value from the URL
#####
# redirect_uri = 'http://localhost'
# scope = ['activity:read_all']
# authorize_url = 'https://www.strava.com/oauth/authorize'
# oauth = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri, scope=scope)
# print(oauth.authorization_url(authorize_url))
# sys.exit()
#####


#####
# STEP 2
# Getting Access Token
# Grab the 'code' value obtained in STEP 1
# Run the code below to obtain the 'access_token'
#####
# token_url = 'https://www.strava.com/api/v3/oauth/token'
# payload = {
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'code': '',
#     'grant_type': 'authorization_code',
# }
# r = requests.post(token_url, data=payload)
# print(r.json())
# sys.exit()
#####


#####
# STEP 3
# Getting list of activities
# Use the obtained access_token in STEP 2
#####
activities_url = 'https://www.strava.com/api/v3/athlete/activities'
token = ''
headers = {
    'Authorization': f'Bearer {token}',
}
params = {
    'after': '1690869600', # Tue Aug 01 2023 06:00:00 GMT+0000
    'per_page': 200,
}
r = requests.get(activities_url, params=params, headers=headers)
# print(r.raise_for_status())
# print(r.json())

f = open("activities.json", "w")
f.write(json.dumps(r.json()))
f.close()
