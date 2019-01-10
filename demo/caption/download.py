import requests
import tqdm
import os
class Downloader:
    def __init__(self,url,target = "dataset"):
        self.url = url
        self.multiple = type(url) == type([])
        self.files = []
        if os.path.basename(target) not in os.listdir(os.path.dirname(target)):
            os.mkdir(target)
        self.target = target
    def download(self):
        if self.multiple:
            for i in self.url:
                name =  _fetch(i)
                print("Downloaded")
    def _fetch(self,url):
        name = url.split("/")[-1]
        response = requests.get(url,stream = True)
        path = os.path.join(self.target,name)
        with open(path,"wb") as f:
            for i in tqdm(response.iter_content(chunk_size = 1024)):
                if chunk:
                    f.write(i)
    def _extract(self):
        pass
