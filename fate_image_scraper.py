import requests
from bs4 import BeautifulSoup

servant_list = ["quetzalcoatl", "jeanne-darc-alter", "bradamante", "brynhild", "ivan-terrible"]
src_list = []
count = 0

for i in servant_list:
    servant_url = "https://gamepress.gg/grandorder/servant/" + i
    r = requests.get(servant_url)
    soup = BeautifulSoup(r.text, features="html.parser")
    images = soup.find_all(class_="image-style-servant-image")
    for img in images:
        src = img.get("src")
        if src:
            src_list.append(src)

for link in src_list:
    count += 1
    image_url = "http://gamepress.gg" + link
    r2 = requests.get(image_url)
    with open(str(count) + "image.png", "wb") as f:
        f.write(r2.content)
