import requests
from bs4 import BeautifulSoup


f = open('pmid.txt', 'r')
PMIDs = [line.rstrip() for line in f if len(line.rstrip()) is not 0]
f.close()

full_links = []   
for pmid in PMIDs:
    url = "http://www.ncbi.nlm.nih.gov/pubmed/?term=" + pmid
    
    # Sends a GET request. Returns Response object
    r = requests.get(url)
    
    # r.content -- in bytes
    data = BeautifulSoup(r.content)   
    
    # find the link to the full article
    data_link = data.find_all("a", title="Full text at publisher's site")
    for link in data_link:
        full_text_link = link.get("href")
        
        r2 = requests.get(full_text_link)
        
        data2 = BeautifulSoup(r2.text)
        
        for email in data2.find_all("a", attrs={"title":"Link to email address"}):
            print 'pmid: ',pmid, "email: ", email.text
