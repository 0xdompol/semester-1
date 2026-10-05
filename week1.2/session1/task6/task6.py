# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

Artists = {
    "Metallica": [
        {"Ride The Lightning": "27/07/1984"}, {"And Justice For All": "07/09/1988"}, {"Master of Puppets": "03/03/86"}
    ], 
    "Kanye West": [
        {"Bully": "28/03/2026"}, {"Graduation": "11/09/2007"}, {"Vultures II": "03/08/2024"}
    ],
    "Mac Miller": [
        {"Swimming": "03/08/2018"},{"Kids": "13/08/2010"},{"Circles": "17/01/2020"}
    ]
}

# Pretty-print the data structure
pprint(Artists)
# Display details of one album recorded by a specific artist
def display_details(artist, album):
    for album_dict in Artists[artist]:
        if album in album_dict:
            print(album_dict[album])

display_details("Kanye West", "Bully")