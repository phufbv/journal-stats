import requests
from BeautifulSoup import BeautifulSoup


def build_url(journal, volume, issue, number):
	
	base_url = "http://iopscience.iop.org/article/10.3847/" 

	if journal == "ApJ":
		vol_issue_num = str(volume) + "/" + str(issue) + "/" + str(number)
		
		pre_vol_833 = "0004-637X/"
		post_vol_833 = "1538-4357/"
	
	elif journal == "ApJL":
		vol_issue_num = str(volume) + "/" + str(issue) + "/" + 'L' + str(number)
		
		pre_vol_833 = "2041-8205/"
		post_vol_833 = "2041-8213/"


	# URLs slightly different before vol.833 iss.2 for some reason
	if volume > 833:
	    url = base_url + post_vol_833 + vol_issue_num
	else:
	    url = base_url + pre_vol_833 + vol_issue_num

	return url


def get_date_div(url):
	    
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	        
	dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'}).text
	#dates = soup.find('div', attrs={'class':'article-meta'})

	return dates
