# THE POPULARITY OF ARTISTS ON SPOTIFY
#### Video Demo: <https://youtu.be/hYVE7LrDOdQ?si=iMZPkmfSWyHNJxp0>
#### Description:

Welcome to my first project that was created for completing CS50's Introduction to Programming with Python.
Spotify gives a number between 0 and 100 for each artist, with 100 being the most popular. The artist's popularity score is calculated from the popularity of all the artist's tracks. This number can be extracted only from Spotify's API. <https://developer.spotify.com/>. I created a code that shows the popularity score of artists on Spotify. It arranges the artists in order of popularity, starting with the most popular. The result is printed in a table which has two columns: name and popularity. You will also get some mathematical statistics of the popularity scores below.

You can type as many artists as you want by using their Sporify ID to get information about their popularity scores. A Spotify ID, for example: "711MCceyCBcFnzjGY4Q7Un?si=k2hYkDkWSUi4ztlowVnOcg", can be found at the end of the URL of the artist on Spotify. If you finish typing each artist you wanted, just type 'exit' and the program will exit.

To use this program, you will need a Spotify API access token. Each access token is valid only for one hour. You can get information on how to request an access token on this website: <https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token>

#### My files in the folder:

There exist four files in my folder called project: project.py, test_project.py, requirements.txt and README.md.

My main function and five additional functions (get_artist_data, get_artist_dict, sorted_artists_list, get_table, get_statistics) are found in the file project.py.

Three functions (get_artist_dict, sorted_artists_list, get_statistics) are accompanied by tests (test_get_artist_dict, test_get_artist_dict_integer, test_sorted_artists_list, test_sorted_artists_list_exception, test_get_statistics, test_get_statistics_exception). These tests can be found in the file test_project.py.

The pip-installable libraries that my project requires are indicated in the file requirements.txt. The description of my project can be read in the file README.md.

#### The main function of my project:

The main function requires the user to get a valid access token to access the artists' data on Spotify.

Afterwards, by using a 'while True' loop, the user is able to type as many artists' Spotify IDs as they want. Function called get_artist_data identifies the artist by its Spotify ID, and gives access to information for the artist. The 'while True' loop will finish, if the user types 'exit'. During the 'while True' loop, dictionaries of artists are being created by the function called get_artist_dict. These dictionaries have two keys: name and popularity. The value of name is the artist's name, and the value of popularity is the artist's popularity score, which becomes an integer.

These dictionaries are appended to a list. This list becomes the list of artists. Each of its elements is a dictionary. The main function uses the function called sorted_artist_list so that the artists' dictionaries are getting sorted by their popularity scores.

Finally, the created list is being called by the tabulate function from the tabulate library, in order to get a nice chart of the artists' names and popularity scores, in order of popularity.

By calling the function called get_statistics, some mathematical statistics such as the popularity scores' mean, median and mode are being printed below the chart.

#### Summary:

This program is useful for comparing artists according to their popularities, getting to know popularity scores of our favourite musicians, or just having fun looking for the most popular and the least popular artists in the World. ☺️
