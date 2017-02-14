import requests
from BeautifulSoup import BeautifulSoup

apj_base = "http://iopscience.iop.org/article/10.3847/1538-4357/"
apj_base2 = "http://iopscience.iop.org/article/10.3847/0004-637X/"  # different base URL before vol.833 iss.2 for some reason

latest_volume = 836  # same for both ApJ and ApJL - issues run in parallel

volume_list = range(latest_volume-11,latest_volume+1)  # latest 12 volumes, roughly 6 months


num_articles = 1  # test using a few articles

for volume in reversed(volume_list):

	vol_issue = str(volume) + "/1/"

	for num in range(1,num_articles+1):

		if volume > 833:
			url = apj_base + vol_issue + str(num)
		else:
			url = apj_base2 + vol_issue + str(num)
	    
		try:
			r = requests.get(url)
			soup = BeautifulSoup(r.content)
	        
			dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'}).text
			#dates = soup.find('div', attrs={'class':'article-meta'})

			start = dates.find("Received ") + 9
			end = dates.find("Accepted")
	    
			received_date = dates[start:end]
	    
			start = dates.find("Accepted ") + 9
			end = dates.find("Published")
	    
			accepted_date = dates[start:end]
	    
			print received_date, accepted_date
	    
		except:
			print "Some error occurred (URL '",url,"' not available?). Skipping."
