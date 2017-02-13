import requests
from BeautifulSoup import BeautifulSoup

apj_base = "http://iopscience.iop.org/article/10.3847/1538-4357/"

latest_issue = "836/1/" #same for both ApJ and ApJL - issues run in parallel


num_articles = 5 #test using a few articles

for num in range(1,num_articles+1):
    url = apj_base + latest_issue + str(num)
    
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
    
