#tuto video https://www.youtube.com/watch?v=xdq6Gz33khQ

import os
os.system('pip install requests')
import requests
import datetime
import base64

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

client = SpotifyAPI(client_id, client_secret)
client.perform_auth()
