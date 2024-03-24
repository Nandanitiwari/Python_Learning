#Command Line utility
import argparse
import requests

def download_file(url, local_filename):
    # local_filename = url.split('/')[-1]
    #Note the stream=True parameter below
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 8192):
                #if you lhave chunk encoded response uncomment if
                #and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

#Add command line argument
parser.add_argument("Url", help = "Url of the file to download")

parser.add_argument("-o", "--output", help = "Name of the file", default=None)

#Parse the arguments
args = parser.parse_args()

#Use the arguments in your code
print(args.Url)
print(args.output)
download_file(args.Url, args.output)


#python 38\109.py https://www.thebluediamondgallery.com/handwriting/images/index.jpg -o zindex.py       