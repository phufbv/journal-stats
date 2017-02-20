# Select journal - must be either "ApJ" or "ApJL"
journal = "ApJ"

# Name of output file
filename = journal + "_dates.csv"

# Number of articles to use from each issue
num_articles = 30

# Which issue number to sample in each volume
issue = 1

# Number of volumes to use
num_volumes = 18  # 18 volumes per year




from datetime import datetime
current_year = datetime.now().year

volume_directory = {
	'2017':'836',
	}

latest_volume = 836  # same for both ApJ and ApJL - issues run in parallel

volumes = range(latest_volume-num_volumes+1,latest_volume+1)
