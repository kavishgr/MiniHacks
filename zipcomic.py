from bs4 import BeautifulSoup
import requests as req
from sys import argv
from pathlib import Path
import subprocess as sp
import os

# directory where you store your comic books
comic_home_dir = "/Users/kavish/Downloads/comic/comics/"

url = argv[1]
links = []



# first
def mkdir(url):
    os.chdir(comic_home_dir)
    p = Path(url)
    p = p.name
    if "-" in p:
        p = p.replace("-", " ").title()
    os.mkdir(p)
    os.chdir(p)

# second
def get_all_links(url):
    resp = req.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('a'):
        href = link.get("href")
        if href.startswith("/storage"):
            newurl= "https://www.zipcomic.com" + href
            links.append(newurl)

# third

def download(links):
    file = 0
    for link in links:
        file += 1
        sp.run(f"wget -O {file}.cbr {link} -q --show-progress", shell=True)


mkdir(url)
get_all_links(url)
download(links)

