import requests as rq
from bs4 import BeautifulSoup as BS

history = []
prefix = "http://cspro.sogang.ac.kr/~gr120170213"
index = 1

urlFile = open("URL.txt", "w")

def crawl(url):
    global index
    try:
        r = rq.get(url)
        r.raise_for_status()

        if r.content in history:
            return
        history.append(r.content)
        urlFile.write(url + "\n")

        soup = BS(r.content, "html.parser")

        outputFile = open("Output_{:04d}.txt".format(index), "w")
        index += 1
        outputFile.write(soup.text)
        outputFile.close()

        result = soup.find_all('a')
        for a in result:
            link = a.get("href")
            if link[0:7] == "http://":
                crawl(link)
            else:
                crawl(prefix + "/" + link)

    except:
        return

crawl("http://cspro.sogang.ac.kr/~gr120170213/")
urlFile.close()
