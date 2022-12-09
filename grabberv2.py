import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter
import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import urllib.request 

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry(f"{800}x{500}")
app.title("Minimal Spotify Data Collector")
app.configure(background = 'white')
link_var = tk.StringVar()

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='86a607d1c9754bf4b133b0c7f005ae48', client_secret='f055259507c34fd08186fb1f06fdae2f'),)

#FUNCTIONS
def search_fun():
    linko = link_var.get()
    results = spotify.artist_albums(linko, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
    albums.extend(results['items'])
    label = customtkinter.CTkLabel(master=app, text="TOP Album : ")
    label.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
    for album in albums:
        text_var1 = tkinter.StringVar(value= album['name'])

    label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var1,
                               width=220,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    #To get top tracks
    results = spotify.artist_top_tracks(linko)
    for track in results['tracks'][:1]:
        text_var2 = tkinter.StringVar(value= track['name'])
    
    label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var2,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
    label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    label = customtkinter.CTkLabel(master=app, text="Top Song : ")
    label.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
    
"""""
    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()
"""""


#Label_For_Pasting_YT_Links
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Paste Artist Spotify URI : ",
                               textvariable=link_var,
                               width=500,
                               height=35,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.4, rely=0.3, anchor=tkinter.CENTER)

#Search_Button
button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=35,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Search",
                                 command=search_fun)
button.place(relx=0.9, rely=0.3, anchor=tkinter.CENTER)

app.mainloop()

"""""

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='86a607d1c9754bf4b133b0c7f005ae48', client_secret='f055259507c34fd08186fb1f06fdae2f'),)
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
 results = spotify.next(results)
 albums.extend(results['items'])
for album in albums:
 print(album['name'])

"""""