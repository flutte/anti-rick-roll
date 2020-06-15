from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/watch?v=3DxXa2lWPz0' # url to yt link here

# Keywords to check for
keywords = [
    'Rick Astley',
    'rickroll',
    'rick',
    'astley',
    'Never gonna',
    'Give you up',
    'Never gonna give you up'
]

content = requests.get(url)

soup = BeautifulSoup(content.content, 'html.parser')
text = soup.get_text().lower()


for keyword in keywords:
    if keyword.lower() in text:
        print("Video contains rickroll!")
        break
