from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

html_doc = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(html_doc, 'html.parser')

songs = soup.find_all("span", class_="chart-element__information__song")
song_text = [i.getText() for i in songs]
print(song_text)











#TODO: 1. Scrape the Billboard Hot 100 for the songs of a particular date.✅
#TODO: 2. Authenticate with Spotify
#TODO: 3. Search Spotify with the scraped songs from Todo 1
#TODO: 4. Create and add a spotify playlist.
