import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import os

def get_youtube_url(song_name):
    split_name = song_name.split()
    url = "https://" + split_name[0] #adds first part of song name to url
    for word in split_name[1:]:
        url = url + "-" + word
    url_end = ".mp3juices.icu/"
    url = url + url_end
       
    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    tag = soup.li
    yt_ref = tag.attrs
    ref_value = yt_ref["yt"]

    #create youtube url
    first = "https://youtu.be/"
    last = ref_value
    yt_url = first + last
    return yt_url

def download_song(youtube_url):
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=".")
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

def read_playlist(playlist_name):
    with open(playlist_name) as playlist_file:
        lines = playlist_file.readlines()
    for line in lines:
        youtube_url = get_youtube_url(line)
        print("downloading " + line)
        print(youtube_url)
        download_song(youtube_url)        


read_playlist("spotify_playlist.txt" #enter your playlist name here)








