import multiprocessing
import requests

def downloadFile(url, name):
    response = requests.get(url)
    open(f"41/album1/file{name}.jpg", "wb").write(response.content)
 

url = "https://picsum.photos/2000/3000"
for i in range(5):
    downloadFile(url, i)
   