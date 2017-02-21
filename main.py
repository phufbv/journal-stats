import parameters as pars
import html

from file_writer import FileWriter
from article import Article


writer = FileWriter(pars.filename)

for volume in reversed(pars.volumes):

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
