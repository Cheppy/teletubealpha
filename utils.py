import requests
import wget
from bs4 import BeautifulSoup
import youtube_dl
import ffmpeg

import os


def get_pic(link):
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, 'lxml')

    for x in soup.find_all("meta", property="og:image"):
        return x['content']


def show_pic(url):
    imb = wget.download(get_pic(url))
    return imb


def is_size_ok(path, max_allowed=5e10):
    return os.path.getsize(path) < max_allowed


def get_vid(url):
    ydl_opts = {'merge_output_format': ''}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        result = ydl.extract_info(url, download=False)
        outfile = ydl.prepare_filename(result)[:-1] + "mp4"

    return str(outfile)
