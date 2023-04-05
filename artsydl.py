import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlparse, parse_qs
import subprocess as sp
import os

url = sys.argv[1] # takes a url(inside quotes) as argument
domain = urlparse(url).netloc # extract domain name from url
reqs = requests.get(url) # save http response 
soup = BeautifulSoup(reqs.text, 'html.parser') # parse it in beautifulsoup to extract data


def getArtworksUrlsPlusTitle():
    urls = []
    for links in soup.find_all('a'):
        link = links.get('href')
        if link.startswith("/artwork"):
            fullurl = f"https://{domain}{link}"
            urls.append(fullurl)
    cleanurls = set(urls) # remove duplicate lines, returns a dict
    artworks = (list(cleanurls)) # convert the dict into a list
    title = soup.find('title')
    title = title.string
    return artworks, title

def getArtworksJpegs(artworks):
    temp_dictionary = {}
    for artwork in artworks:
        reqs = requests.get(artwork)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        results = soup.findAll('link')
        for result in results:
            url = result['href']
            if url.endswith("jpg"):
                spliturl = urlparse(url)
                dict_result = parse_qs(spliturl.query)
                extractsrc = str(dict_result['src'][0])
                temp_dictionary[f"{extractsrc}"]=f"{artwork.rsplit('/', 1)[1]}"
    return temp_dictionary

def downloadJpegs(artworksjpegs, title):
    os.mkdir(title)
    os.chdir(title)
    for jpeg in artworksjpegs:
        sp.run(f"wget -O '{artworksjpegs[jpeg]}.jpeg' '{jpeg}' -q --show-progress", shell=True)



artworks, title = getArtworksUrlsPlusTitle()
artworksjpegs = getArtworksJpegs(artworks)
downloadJpegs(artworksjpegs, title)



