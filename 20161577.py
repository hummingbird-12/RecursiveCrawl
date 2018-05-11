import requests as rq
from bs4 import BeautifulSoup as BS
import sys

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
        print(url)
        urlFile.write(url + "\n")
        history.append(r.content)
        soup = BS(r.content, "html.parser")
        try:
            outputFile = open("./output/Output_{:04d}.txt".format(index), "w")
            index += 1
            outputFile.write(soup.text)
            #outputFile.writelines(i.get_text() + "\n" for i in soup.find_all('p'))
            outputFile.close()
        except:
            print(sys.exc_info()[0])
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
