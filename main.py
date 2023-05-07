import requests
from bs4 import BeautifulSoup


URL = "https://www.jiosaavn.com/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

songs = soup.find_all(name="a", class_="u-ellipsis u-color-js-gray")

trending_song = [i.getText() for i in songs]

with open("HomePage_List.txt", mode="w", encoding="utf-8") as file:
    for i in trending_song:
        file.write(f"{i}\n")