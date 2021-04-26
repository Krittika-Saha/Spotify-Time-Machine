from bs4 import BeautifulSoup
import requests

html_doc = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(html_doc, 'html.parser')















#TODO: 1. Scrape the Billboard Hot 100 for the songs of a particular date.
#TODO: 2. Authenticate with Spotify
#TODO: 3. Search Spotify with the scraped songs from Todo 1
#TODO: 4. Create and add a spotify playlist.
