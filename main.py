import parameters
import html


for volume in reversed(parameters.volume_list):

	for number in range(1,parameters.num_articles+1):

		url = html.build_url(volume, parameters.issue, number)
	    
		try:
			dates = html.get_date_div(url)
		except:
			print "Some error occurred (URL '",url,"' not available?). Skipping."
			break


		start = dates.find("Received ") + 9
		end = dates.find("Accepted")
	    
		received_date = dates[start:end]
	    
		start = dates.find("Accepted ") + 9
		end = dates.find("Published")
	    
		accepted_date = dates[start:end]
	    
		print received_date, accepted_date
	    