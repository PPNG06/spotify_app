#tuto video https://www.youtube.com/watch?v=xdq6Gz33khQ time:42:18

import os
os.system('pip install requests')
import requests
import datetime
import base64
from urllib.parse import urlencode

client_id = "1b24afb4761649179023db1f4a95b37a"
client_secret = "8d3a958aa1b34aa6981f572a30b8a5c7"

class SpotifyAPI(object):

    access_token = None
    access_token_expires = None
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        returns a base64 encoded STRING
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("YOU MUST SET CLIENT_ID AND CLIENT_SECRET")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization":f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type":"client_credentials",
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()

        r = requests.post(token_url, data=token_data, headers=token_headers)

        if r.status_code in range(200,299):
            print("REQUEST VALID")
            data=r.json()
            now = datetime.datetime.now()
            access_token = data['access_token']
            self.access_token = access_token
            expires_in = data['expires_in'] #seconds
            expires = now + datetime.timedelta(seconds=expires_in)
            self.access_token_expires = expires
            did_expire = expires < now
            self.access_token_did_expire = did_expire

            return True

        return False

spotify = SpotifyAPI(client_id, client_secret)
spotify.perform_auth()
access_token = spotify.access_token

headers = {
    "Authorization":f"Bearer {access_token}"
}

'''
search_endpoint = "https://api.spotify.com/v1/search"
search_data = urlencode({"q":"Big Michael", "type":"track","limit":1})
search_url = f"{search_endpoint}?{search_data}"
print(search_url)
search_r = requests.get(search_url, headers=headers,)
print(search_r.status_code)
##print(search_r.json())
track_id_str = search_r.json()['tracks']['items'][0]['id']
track_name = search_r.json()['tracks']['items'][0]['name']
print(track_id_str)
print(track_name)
'''


'''
search_endpoint = "https://api.spotify.com/v1/search"
search_data = urlencode({"q":"Big Michael", "type":"track","limit":1})
search_url = f"{search_endpoint}?{search_data}"
print(search_url)
search_r = requests.get(search_url, headers=headers,)
print(search_r.status_code)
##print(search_r.json())
track_id_str = search_r.json()['tracks']['items'][0]['id']
track_name = search_r.json()['tracks']['items'][0]['name']
print(track_id_str)
print(track_name)
'''


'''
genres_endpoint = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
genres_url = f"{genres_endpoint}?"
genres_r = requests.get(genres_url,headers=headers)
interesting_indexes = [0,1,4,5,8,16,17,18,20,21,26,27,30,31,32,33,34,37,38,44,46,47,48,49,51,52,53,55,64,66,67,68,69,70,73,77,80,81,83,85,86,95,97,98,99,100,102,103,104,105,110,114,115,116,120,-2,-1]
genres = []
for index in interesting_indexes:
    genres.append(genres_r.json()['genres'][index])
print(genres)
'''


'''
recommendation_endpoint = "https://api.spotify.com/v1/recommendations"
recommendation_data = urlencode({"seed_tracks":track_id_str,})
recommendation_url=f"{recommendation_endpoint}?{recommendation_data}"
recommendation_r = requests.get(recommendation_url,headers=headers,)
x=0
for r in recommendation_r:
    print(recommendation_r.status_code)
    print(recommendation_r.json()['tracks'][x]['name'])
    x+=1
'''
