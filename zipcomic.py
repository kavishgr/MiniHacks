import argparse
from bs4 import BeautifulSoup
import requests as req
from sys import argv
from pathlib import Path
import subprocess as sp
import os

def calculate_range(rangearg):
    split_range = rangearg.split(':')
    fromN = int(split_range[0])
    toN = int(split_range[1])
    if fromN > 0:
        fromN -= 1
    return fromN, toN

def mkdir(url):
    os.chdir(comic_home_dir)
    p = Path(url)
    p = p.name
    if "-" in p:
        p = p.replace("-", " ").title()
    try:
        os.mkdir(p)
    except FileExistsError:
        print(f"Directory: '{p}' already exists!")
    os.chdir(p)

def get_all_links(url):
    resp = req.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('a'):
        href = link.get("href")
        if href.startswith("/storage"):
            newurl= "https://www.zipcomic.com" + href
            links.append(newurl)

def downloadtest(links, rangearg):
    fromN = 0
    toN = 0
    if rangearg:
        fromN, toN = calculate_range(rangearg)
        links = links[fromN:toN]
        for link in links:
            fromN += 1
            sp.run(f"wget -O {fromN}.cbr {link} -q --show-progress", shell=True)
    else:
        for link in links:
            fromN += 1
            sp.run(f"wget -O {fromN}.cbr {link} -q --show-progress", shell=True)


#### MAIN ####

comic_home_dir = "/Users/kavish/Downloads/comic/comics/"
links = []

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Specify a url", type=str)
parser.add_argument("-r", "--range", help="Specify a range. E.g 3:11", type=str)
args = parser.parse_args()

rangearg = args.range
url =  args.url

mkdir(url)
get_all_links(url)
downloadtest(links, rangearg)



