import requests
from bs4 import BeautifulSoup
import os
import time

TIMEOUT_TIME = 60

def search_images(species, start):
    url = rf"https://www.google.no/search?q={species}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982&num=100&start={start}"
    response = requests.get(url, timeout=TIMEOUT_TIME)
    if response.status_code != 200:
        print(f"[ERR] Failed to request URL page for `{species}`.")
    else:
        print(f"Successfully requested URL page for `{species}` [{int(start/20)+1}/5]...")
        page = response.text
        soup = BeautifulSoup(page, "html.parser")
        for img_block in soup.find_all("img", limit=50):
            img_url = img_block.get("src")
            if img_url.startswith("https://"):
                img_path = "data/{}/img_{}.jpg".format(species, img_url[-8:])
                try:
                    download_img(img_url, img_path)
                except FileNotFoundError:
                    dir_path = "data/{}".format(species)
                    os.mkdir(dir_path)
                    download_img(img_url, img_path)

def download_img(img_url, path):
    response = requests.get(img_url, timeout=TIMEOUT_TIME)
    time.sleep(0.5)
    if response.status_code != 200:
        print(f"[ERR] Failed to download image from `{img_url}`.")
    else:
        with open(path, "wb") as file:
            file.write(response.content)
            print(f"Image `{img_url}` downloaded succesfully...")

species_path = "species.txt"
with open(species_path, "r") as file:
    contents = []
    for line in file.readlines():
        contents.append(line.rstrip())


for mushroom_name in contents:
    for start in range(0, 81, 20):
        search_images(mushroom_name, start)
        time.sleep(0.5)