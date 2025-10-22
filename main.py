from check_twitch import get_streamers

### The streamers we're wanting to find ###
streamer_list = [
    "ThePrimeagen",
    "Teej_TV",
    "Mad_Magz_",
    "Sir__Knight_",
    "CriticalRole"
]

class FindStreamers():
    def __init__(self):
        super().__init__()
        streamers_info = get_streamers(streamer_list)
        
        for streamer in streamers_info:
            print(streamer["user_name"]+": "+streamer["title"])
            print("https://twitch.tv/" + streamer["user_name"])

if __name__ == "__main__":
    streams = FindStreamers()
