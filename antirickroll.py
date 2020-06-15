from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com/watch?v=3DxXa2lWPz0' # url to yt link here

# Keywords to check for
keywords = []

try:
    with open("keywords.txt") as f:
        for line in f.read():
            keywords.append(line)
except FileNotFoundError:
    print("Create keywords.txt in . and put atleast 1 keyword")
    input()
    exit()

content = requests.get(url)

soup = BeautifulSoup(content.content, 'html.parser')
text = soup.get_text().lower()


for keyword in keywords:
    if keyword.lower() in text:
        print("Video contains rickroll!")
        break
