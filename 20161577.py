import requests as rq               # import requests module
from bs4 import BeautifulSoup as BS # import BeautifulSoup4 module

history = [] # list used to save request history
prefix = "http://cspro.sogang.ac.kr/~gr120170213" # prefix for URLs
index = 1 # crawl output file index

urlFile = open("URL.txt", "w") # file to write visited URLs

# recursive function for crawling
# parameter : url -> URL of site to crawl
def crawl(url):
    global index # index is a global variable
    try:
        r = rq.get(url)      # get request from URL
        r.raise_for_status() # raise exception flags, if any

        if r.content in history: # check history to avoid visiting more than once
            return # if already visited before, return
        history.append(r.content) # append request content to history
        urlFile.write(url + "\n") # write URL into URL.txt

        soup = BS(r.content, "html.parser") # parse request content as HTML

        outputFile = open("Output_{:04d}.txt".format(index), "w") # open crawl output file
        outputFile.write(soup.text) # write into file 
        outputFile.close() # close file
        index += 1 # increase output file index

        result = soup.find_all('a') # find all <a> tags in HTML and create list
        for a in result: # for each <a> tag
            link = a.get("href") # get link from href field
            if link[0:7] == "http://": # if link starts with "http://"
                crawl(link) # crawl link
            else: # if link does NOT start with "http://"
                crawl(prefix + "/" + link) # append to prefix and crawl link
    except: # if any exception flag is raised, do NOT crawl
        return

crawl("http://cspro.sogang.ac.kr/~gr120170213/") # start crawl from root page
urlFile.close() # close URL.txt file
