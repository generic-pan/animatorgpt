from requests_oauthlib import OAuth2Session

import freesound
import pandas as pd


# do the OAuth dance
oauth = OAuth2Session(client_id)

authorization_url, state = oauth.authorization_url(
    "https://freesound.org/apiv2/oauth2/authorize/"
)
print(f"Please go to {authorization_url} and authorize access.")

authorization_code = input("Please enter the authorization code:")
oauth_token = oauth.fetch_token(
    "https://freesound.org/apiv2/oauth2/access_token/",
    authorization_code,
    client_secret=client_secret,
)

df = 

client = freesound.FreesoundClient()
client.set_token(oauth_token["access_token"], "oauth")

for index, row in df.iterrows():
    results = client.text_search(query="farming",filter='license:"Creative Commons 0" type:"wav"',fields="id,name")

    for i in range(5):
        if i < len(results):
            sound = results[i]
            formatted = sound.name.replace(" ","_") + '.wav'
            sound.retrieve(f"freesound/{formatted}")
        else:
