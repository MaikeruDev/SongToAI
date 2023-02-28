 
import re
import os
import time
import json
import openai 
import requests 
from lyricsgenius import Genius

print("Song Name:")
song_name = input()

path = "./results/" + song_name.replace(" ", "_") + "/"
if not os.path.exists(path): os.mkdir(path)

print("Artist:")
artist = input()

f = open('./secret.json')

secret = json.load(f) 

openai.api_key = secret["OPENAI_KEY"]
 
genius = Genius(secret["GENIUS_KEY"])
 
song = genius.search_song(song_name, artist)
 
lyrics = re.sub(r'\[.*?\]|\(.*?\)', '', song.lyrics)
 
lyrics = re.sub(r'\((.*?)\)\s*\1+', r'\1', lyrics)
 
lines = [line.strip() for line in lyrics.splitlines() if line.strip()]
 
lines.pop(0)
 
if lines[-1].startswith('Outro:'):
    lines.pop()
else:
    lines.pop(-1)
 
final_lyrics = '\n'.join(lines)

i = 1

for lyric in final_lyrics.split('\n'):
    try:
        response = openai.Image.create(
        prompt=lyric,
        n=4,
        size="1024x1024",
        )
        image_url = response['data']   

        if not os.path.exists(path + str(i)): os.mkdir(path + str(i))

        img_data = requests.get(image_url[0]['url']).content
        with open(path + str(i) + '/1.jpg', 'wb') as handler:
            handler.write(img_data)
        img_data = requests.get(image_url[1]['url']).content
        with open(path + str(i) + '/2.jpg', 'wb') as handler:
            handler.write(img_data)
        img_data = requests.get(image_url[2]['url']).content
        with open(path + str(i) + '/3.jpg', 'wb') as handler:
            handler.write(img_data)
        img_data = requests.get(image_url[3]['url']).content
        with open(path + str(i) + '/4.jpg', 'wb') as handler:
            handler.write(img_data)
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)
 
    i = i + 1
    print(lyric)