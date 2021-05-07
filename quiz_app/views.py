from django.shortcuts import render
from quiz_app.forms import UserForm
from music_app.models import Artist
from music_app.models import Music
import random
import os
os.system('pip install requests')
os.system('pip install Pillow')
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

spotify = SpotifyAPI(client_id,client_secret)
spotify.perform_auth()
access_token = spotify.access_token

headers = {
    "Authorization":f"Bearer {access_token}"
}
# Create your views here.
def show_basic(request):
    return render(request,'quiz_app/basic.html')


def index(request):
    return render(request,'quiz_app/homepage.html')


def show_music_page(request, form_instance):

    cleaned_data = super(UserForm, form_instance).clean()
    print(cleaned_data)
    recommendation_endpoint = "https://api.spotify.com/v1/recommendations"

    energy = float(cleaned_data['mood'])
    print(energy)

    genres_list = [cleaned_data['style1']]
    if cleaned_data['style2'] != "-":
        genres_list.append(cleaned_data['style2'])
    if cleaned_data['style3'] != "-":
        genres_list.append(cleaned_data['style3'])
    print(genres_list)
    recommendation_data = {"seed_genres":genres_list,"target_energy":energy}
    if cleaned_data["artist"] != "0" and cleaned_data["artist"] != "":
        search_endpoint = "https://api.spotify.com/v1/search"
        search_data = urlencode({"q":cleaned_data['artist'], "type":"artist","limit":1})
        search_url = f"{search_endpoint}?{search_data}"
        ##print(search_url)
        search_r = requests.get(search_url, headers=headers,)
        #3print(search_r.status_code)
        ##print(search_r.json())
        ##print(search_r.json()['artists']['items'][0]['name'])
        artist_id_str = search_r.json()['artists']['items'][0]['id']
        artist_name = search_r.json()['artists']['items'][0]['name']
        ##print(artist_id_str)
        recommendation_data["seed_artists"] = artist_id_str

    if cleaned_data["linked_track"] != "0" and cleaned_data["linked_track"] != "":
        search_endpoint = "https://api.spotify.com/v1/search"
        search_data = urlencode({"q":cleaned_data['linked_track'], "type":"track","limit":1})
        search_url = f"{search_endpoint}?{search_data}"
        search_r = requests.get(search_url, headers=headers)
        linked_track_id_str = search_r.json()['tracks']['items'][0]['id']
        linked_track_id_name = search_r.json()['tracks']['items'][0]['name']
        recommendation_data["seed_tracks"] = linked_track_id_str


    recommendation_data_url = urlencode(recommendation_data)
    recommendation_url=f"{recommendation_endpoint}?{recommendation_data_url}"
    ##print(recommendation_url)
    recommendation_r = requests.get(recommendation_url,headers=headers,)


    print(recommendation_r.json())
    ##for r in recommendation_r.json()['tracks']:

        ##print(recommendation_r.status_code)
        ##print(r['name'])
        ##print(r['artists'][0]['name'])
    a_dict = {"music":[]}
    Artist.objects.all().delete()
    Music.objects.all().delete()
    for r in recommendation_r.json()['tracks']:
        artists = Artist.objects.get_or_create(name=r['artists'][0]['name'],)[0]
        musics = Music.objects.get_or_create(artist=artists,style=genres_list,mood=energy,title=r['name'],link=r['external_urls']['spotify'])[0]


    if cleaned_data["artist"] != "0" and cleaned_data["artist"] != "" and cleaned_data["linked_track"] != "0" and cleaned_data["linked_track"] != "":
        a_dict = {"music":Music.objects.order_by("mood"),"seed_artist":artist_name,"seed_track":linked_track_id_name}

    elif cleaned_data["artist"] != "0" and cleaned_data["artist"] != "":
        a_dict = {"music":Music.objects.order_by("mood"),"seed_artist":artist_name}

    elif cleaned_data["linked_track"] != "0" and cleaned_data["linked_track"] != "":
        a_dict = {"music":Music.objects.order_by("mood"),"seed_track":linked_track_id_name}

    else:
        print("ERROR NO ARTIST NO TRACK")

    return render(request,'quiz_app/musicpage.html',context=a_dict)


def show_mainpage(request):
    form_instance = UserForm()
    if request.method == 'POST':
        print(request.POST)
        form_instance = UserForm(request.POST)

        if form_instance.is_valid():
            form_instance.save()
            return show_music_page(request,form_instance)

        else:
            print("problem")
    ##return render(request,'quiz_app/homepage.html')
    return render(request,'quiz_app/homepage.html')
