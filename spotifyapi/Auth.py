#tuto video https://www.youtube.com/watch?v=xdq6Gz33khQ

import os
os.system('pip install requests')
import requests
import datetime
import base64

client_id = "1b24afb4761649179023db1f4a95b37a"
client_secret = "8d3a958aa1b34aa6981f572a30b8a5c7"

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type":"client_credentials",
}
token_headers = {
    "Authorization":f"Basic {client_creds_b64.decode()}"
}

r = requests.post(token_url, data=token_data, headers=token_headers)
valid_request = r.status_code in range(200,299)

if valid_request:
    print("REQUEST VALID")
    token_response_data=r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] #seconds
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
