import requests
from BeautifulSoup import BeautifulSoup

apj_base = "http://iopscience.iop.org/article/10.3847/1538-4357/"

latest_issue = "836/1/" #same for both ApJ and ApJL - issues run in parallel


num_articles = 1

for art in range(1,num_articles+1):
	url = apj_base + latest_issue + str(art)
	print url
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	print soup
