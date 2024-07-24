from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
import requests
import pandas as pd


root = Tk()
root.title("anime App")
root.geometry("800x500+300+200")
root.resizable(False, False)


def load_image(image_path, width, height):
    try:
        original_image = Image.open(image_path)
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    except IOError:
        messagebox.showerror("Error", f"Cannot load image {image_path}")
        return None

Search_image = load_image("search field.png", 630, 210)
search_icon = PhotoImage(file="search_icon.png")
logo_image = load_image("logo.png", 200, 160)
frame_image = PhotoImage(file="big box.png")
frame2_image = PhotoImage(file="small box.png")

# API Request
def get_anime_info(anime_name):
    query = '''
    query ($search: String) {
      Media (search: $search, type: ANIME) {
        title {
          romaji
          english
        }
        episodes
        status
        season
        seasonYear
        genres
        relations {
          edges {
            node {
              season
              seasonYear
            }
          }
        }
      }
    }
    '''
    variables = {'search': anime_name}
    url = 'https://graphql.anilist.co' #AniList API you can also use other apis
    response = requests.post(url, json={'query': query, 'variables': variables})

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'Media' in data['data']:
            media = data['data']['Media']
            title = media['title']['romaji'] if media['title']['romaji'] else media['title']['english']
            episodes = media['episodes']
            status = media['status']
            season = media['season']
            season_year = media['seasonYear']
            genres = media['genres']

            # Count distinct seasons
            seasons = {(season, season_year)}
            for edge in media['relations']['edges']:
                node = edge['node']
                if node['season'] and node['seasonYear']:
                    seasons.add((node['season'], node['seasonYear']))

            season_count = len(seasons)

            return {
                'title': title,
                'episodes': episodes,
                'status': status,
                'season_count': season_count,
                'genre': genres[0] if genres else 'N/A'
            }
        else:
            return None
    else:
        return None

# Search for manga chapter in dataset
def get_manga_chapter(anime_name):
    
        df = pd.read_excel('anime data.xlsx') 
        chapter = df.loc[df['title'].str.lower() == anime_name.lower(), 'manga chapter']
        if not chapter.empty:
            return chapter.values[0]
        

# Search Function
def search_anime():
    anime_name = textfield.get()
    anime_info = get_anime_info(anime_name)
    if anime_info:
        w.config(text=anime_info['episodes'])
        h.config(text=anime_info['status'])
        d.config(text=anime_info['season_count'])
        p.config(text=anime_info['genre'])
        
        manga_chapter = get_manga_chapter(anime_name)
        k.config(text=manga_chapter if manga_chapter else 'Synced') # it means that the anime and manga are both synced and finished 
    else:
        messagebox.showerror("Error", "Anime not found or spelled incorrectly")

# Function for Enter key
def on_enter(event):
    search_anime()

# UI strecture
Label(root, image=Search_image).place(x=0, y=0)
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#F2AE7D", border=0, fg="black")
textfield.place(x=90, y=68, width=360, height=50)
Button(root, image=search_icon, borderwidth=0, cursor="hand2", bg="#F2AE7D", command=search_anime).place(x=460, y=68, width=50, height=50)
Label(root, image=logo_image).place(x=570, y=3)
Label(root, image=frame_image).place(x=12, y=155)
Label(root, image=frame2_image).place(x=220, y=330)

Label(root, text="Episode", font=("Helvetica", 15, 'bold'), fg="black", bg="#E66767").place(x=100, y=297)
Label(root, text="Status", font=("Helvetica", 15, 'bold'), fg="black", bg="#E66767").place(x=275, y=297)
Label(root, text="Seasons", font=("Helvetica", 15, 'bold'), fg="black", bg="#E66767").place(x=440, y=297)
Label(root, text="Genre", font=("Helvetica", 15, 'bold'), fg="black", bg="#E66767").place(x=640, y=297)

Label(root, text="pick up manga", font=("Helvetica", 15, 'bold'), fg="black", bg="#E66767").place(x=340, y=440)

w = Label(text=" ", font=("arial", 17, "bold"), bg="#E66767")
w.place(x=120, y=260)
h = Label(text=" ", font=("arial", 17, "bold"), bg="#E66767")
h.place(x=257, y=260)
d = Label(text=" ", font=("arial", 17, "bold"), bg="#E66767")
d.place(x=465, y=260)
p = Label(text=" ", font=("arial", 17, "bold"), bg="#E66767")
p.place(x=610, y=260)
k = Label(text=" ", font=("arial", 17, "bold"), bg="#E66767")
k.place(x=350, y=405)

# tie the Enter key to the search function and icone
textfield.bind('<Return>', on_enter)

root.mainloop()
