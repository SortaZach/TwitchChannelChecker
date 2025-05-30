import httpx
from credentials import CLIENT_ID, CLIENT_SECRET

### Credentials ###
twitch_url = "https://id.twitch.tv/oauth2/token"
get_streams_url = "https://api.twitch.tv/helix/streams"

## NOTE ##
# CLIENT_ID and CLIENT_SECRET are in a different file called
# Credentials that should not live on the actual github.
# If you don't know where to get these values, 
# go to https://dev.twitch.tv/console/apps 
#to register your app and get your credentials.
params = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials"
}

r = httpx.post(twitch_url, data=params)
access_token = r.json()["access_token"]
headers = {
    "Authorization": f"Bearer {access_token}",
    "Client-Id": CLIENT_ID,
}

### Filter For the Streamers We Want To Track ###
def get_streamers(streamers):
    url = makeUrl(streamers)
    streams = httpx.get(url, headers=headers)
    streams.raise_for_status()
    data = streams.json()
    streams_data = data["data"]
    return streams_data 

### Add each Streamer from the list to the url so we get the right information ###
def makeUrl(streamers):
    url = get_streams_url
    count = 0
    for streamer in streamers:
        if count == 0:
            url = url+"?user_login="+streamer
        else:
            url = url+"&user_login="+streamer
        count+=1
    return url

