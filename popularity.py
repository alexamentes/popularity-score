import statistics
from tabulate import tabulate

def main():

    print("\nWelcome to my Final Project for CS50's Introduction to Programming with Python.")
    print("The title of my Final Project: The popularity of artists on Spotify")
    print("Spotify gives a number between 0 and 100 for each artist, with 100 being the most popular.")
    print("The artist's popularity is calculated from the popularity of all the artist's tracks.\n")
    print("My code shows us the popularity score of artists on Spotify.")
    print("It arranges the artists in order of popularity, starting with the most popular.")
    print("You can type as many artists as you want by using their Sporify ID to get information about their popularity scores.\n")
    print("If you finish typing each artist you wanted, just type 'exit' and the program will exit.")
    print("To use this program, you will need a Spotify API access token.")
    print("You can get information how to request an access token on this website:")
    print("https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token\n")


    access_token=input("What is your access token? ")
    artists_list=[]
    popularity_list=[]
    while True:
        artistID=input("What is the artist's Spotify ID? ")
        if artistID!="exit":
            try:
                artist_data=get_artist_data(access_token, artistID)
                artist_dict=get_artist_dict(artist_data["name"], artist_data["popularity"])
                artists_list.append(artist_dict)
                popularity_list.append(int(artist_data["popularity"]))
            except Exception as e:
                print(e)
        else:
            break
    sorted_list=sorted_artists_list(artists_list)
    print(get_table(sorted_list))
    print(get_statistics(popularity_list))


def get_artist_data(access_token, artistID):
    response=requests.get(f"https://api.spotify.com/v1/artists/{artistID}", headers= {"Authorization": f"Bearer  {access_token}"})
    artist_data=response.json()
    return artist_data


def get_artist_dict(name, popularity):
    artist={}
    try:
     artist["name"]=name
     artist["popularity"]=int(popularity)
     return artist
    except ValueError:
       raise ValueError("popularity is not an integer.")


def sorted_artists_list(artists):
    sorted_artists=[]
    try:
        for artist in sorted(artists, key=lambda s: s["popularity"], reverse=True):
            sorted_artists.append(artist)
        return sorted_artists
    except TypeError:
        raise TypeError("There is no key 'popularity'.")

def get_table(artists_list):
    return tabulate(artists_list, headers="keys", tablefmt="grid")

def get_statistics(popularities):
    try:
        mean=statistics.mean(popularities)
        median=statistics.median(popularities)
        modes=statistics.multimode(popularities)
        if len(modes)!=1:
           return f"Mean: {mean:.1f}, median: {median}, mode: no unique mode"
        else:
            for mode in modes:
                return f"Mean: {mean:.1f}, median: {median}, mode: {mode}"
    except statistics.StatisticsError:
        raise statistics.StatisticsError("Statistics error occured.")

if __name__ == "__main__":
    main()
