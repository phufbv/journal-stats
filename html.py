from datetime import datetime
import requests
from BeautifulSoup import BeautifulSoup


def detect_start_volume():
	current_year = datetime.now().year
	
	r = requests.get("http://iopscience.iop.org/journal/0004-637X")
	soup = BeautifulSoup(r.content)

	volumes = soup.find('select', attrs={'id':'allVolumesSelector'}).text  # 'Journal archive' dropdown menu

	# Find first volume of input year
	pos = volumes.rfind(str(current_year))  # index of first occurrence of current year in list of volumes
	vol = int(volumes[pos-5:pos-2])  # get just the number out of the string

	# Find first February volume of current year by adding 2
	start_volume = vol + 2
	
	return (start_volume, current_year-1)


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


def get_article_urls(journal, volume, issue):
	
	base_url = "http://iopscience.iop.org/"

	contentsPageUrl = "http://iopscience.iop.org/issue/0004-637X/" + str(volume) + "/" + str(issue)
	# contents page listing all articles in a given vol. and iss. of the journal

	articleUrls = __get_article_tag(contentsPageUrl)





#	if journal == "ApJ":
#		vol_issue_num = str(volume) + "/" + str(issue)
#		
#		vol = "0004-637X/"
#	
#	elif journal == "ApJL":
#		vol_issue_num = str(volume) + "/" + str(issue)
#		
#		vol = "2041-8205/"

#	url = base_url + vol + vol_issue_num

	return articleUrls[0]


def get_date_div(url):
	    
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	        
	dates = soup.find('div', attrs={'class':'col-no-break wd-jnl-art-dates'}).text
	#dates = soup.find('div', attrs={'class':'article-meta'})

	return dates


def __get_article_tag(url):
	    
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	articleUrls = []

	for article in soup.findAll('a', attrs={'class':'art-list-item-title'}):
		url = article.attrs[0][1]
		articleUrls.append(url.encode('utf-8'))

	return articleUrls

