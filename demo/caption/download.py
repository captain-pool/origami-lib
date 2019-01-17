from __future__ import print_function
import requests
import tqdm
import sys
import os
import errno
import re
from zipfile import ZipFile
class Downloader:
    def __init__(self,url,target = "cocoapi",autoextract = True):
        self._url = url
        self._auto = autoextract
        self.multiple = hasattr(url,'__iter__')
        self.files = []
        if os.path.basename(target) not in os.listdir(os.path.dirname(os.path.abspath(target))):
            os.mkdir(target)
        self.target = os.path.abspath(target)
    def download(self):
        if self.multiple:
            for idx,i in enumerate(self._url):
                print("%d. %s:"%(idx,i)) 
                name =  self._fetch(i)
        else:
            name = self._fetch(self._url)
        print("Downloaded")
        if self._auto:
            self._extract()
    def _fetch(self,url):
        name = url.split("/")[-1]
        response = requests.get(url,stream = True)
        try:
            os.mkdir(os.path.join(self.target,"compressed"))
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(os.path.join(self.target,"compressed")):
                pass
            else:
                raise
        path = os.path.join(os.path.join(self.target,"compressed"),name)
        with open(path,"wb") as f:
            for i in tqdm.tqdm(response.iter_content(chunk_size = 1024)):
                if i:
                    f.write(i)
            self.files.append(path)
        return name
    def _extract(self):
        for i in self.files:
            if "annotations" in os.path.basename(i):
                folder = "annotations"
            else:
                folder = "images"
            year = re.findall("\d+",os.path.basename(i))[-1]
            folder = os.path.join(year,folder)
            try:
                os.makedirs(os.path.join(os.path.dirname(i),folder))
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(folder):
                    pass
                else:
                    raise
            print("Extracting: %s . . . ."%os.path.basename(i),end = "")
            with ZipFile(i,"r") as z:
                z.extractall(path = os.path.join(os.path.dirname(i),folder))
            print("[Extracted]")

