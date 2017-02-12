import requests
from BeautifulSoup import BeautifulSoup
from between import between

apj_base = "http://iopscience.iop.org/article/10.3847/1538-4357/"

latest_issue = "836/1/"  # same for both ApJ and ApJL - issues run in parallel


num_articles = 1  # test using only first article for now

for art in range(1,num_articles+1):
	url = apj_base + latest_issue + str(art)
	
	r = requests.get(url)

	#print r.status_code

	soup = BeautifulSoup(r.content)
	
	dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'})
	#dates = soup.find('div', attrs={'class':'article-meta'})

	print type(dates)
	print type(dates.contents)
	print dates.contents
	




	#print dates.contents.split('Received')
	#print ( (dates.split('Received'))[1].split('<br')[0] )
	
	#print between(dates,'Received: ','<br')
	#print between(dates,'Accepted: ','<br')

