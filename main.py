import sys
import parameters as pars
import html

from article import Article

from file_writer import FileWriter


# Setup output file, and use brief run if testing
writer = FileWriter(pars.filename)
issue = 1  # sample issue for each volume
if len(sys.argv) > 1:
	print "Testing....."
	num_volumes = 1
else:
	num_volumes = 18  # 18 volumes per year


# Sample papers accepted in previous year
date = html.detect_start_volume()
start_volume = date[0]
acceptance_year = date[1]

volumes = range(start_volume-num_volumes+1, start_volume+1)


for volume in reversed(volumes):

	for number in range(1, pars.num_articles+1):

		url = html.build_url(pars.journal, volume, issue, number)
	    
		try:
			date_string = html.get_date_div(url)
		except:
			print "Some error occurred (URL '",url,"' not available?). Skipping."
			break

		article = Article(date_string)

		if article.get_year() == acceptance_year:
			writer.write_to_file(article)

writer.close_file()
