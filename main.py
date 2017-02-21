import parameters as pars
import html

from file_writer import FileWriter
from article import Article


start_volume = html.detect_start_volume()
volumes = range(start_volume-pars.num_volumes+1, start_volume+1)

writer = FileWriter(pars.filename)

for volume in reversed(volumes):

	for number in range(1, pars.num_articles+1):

		url = html.build_url(pars.journal, volume, pars.issue, number)
	    
		try:
			date_string = html.get_date_div(url)
		except:
			print "Some error occurred (URL '",url,"' not available?). Skipping."
			break


		article = Article(date_string)

		writer.write_to_file(article)

writer.close_file()
