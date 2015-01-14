
# objective: parse a pmc page to get emails of the corresponding authors.

import requests
from bs4 import BeautifulSoup

# get a list of PMCIDs by converting PMIDs in CollecTF to PMCID by using 
# http://www.ncbi.nlm.nih.gov/pmc/pmctopmid/

# read PMCIDs from the file
f = open('pmcid.txt', 'r')

PMCs = [line.rstrip() for line in f if len(line.rstrip()) is not 0]

f.close()

# get emails
for pmc in PMCs:
    url = "http://www.ncbi.nlm.nih.gov/pmc/articles/" + pmc + "/"
    r = requests.get(url)

    emails = BeautifulSoup(r.content)

    email_data = emails.find_all("a", {"class":"oemail"})
    for item in email_data:
        print "pmcid: ", pmc, "email: ", item.text[::-1]

