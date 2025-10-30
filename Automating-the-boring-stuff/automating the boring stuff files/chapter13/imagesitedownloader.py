#Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photo, and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
import requests
from bs4 import BeautifulSoup
import os

def download_images(search_term):
    url = f"https://example.com/search?q={search_term}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    
    # find all image elements
    image_tags = soup.find_all("img")
    
    image_urls = []
    for img in image_tags:
        img_url = img.get("src")
        if img_url:
            image_urls.append(img_url)
    
    os.makedirs("images", exist_ok=True)
    
    for i, img_url in enumerate(image_urls, 1):
        # fetch and save image
        content = requests.get(img_url).content
        with open(f"images/{search_term}_{i}.jpg", "wb") as f:
            f.write(content)