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

volume_directory = {}
for year in range(0, 20):
	volume_directory[2015+year] = 800 + (year*num_volumes)

start_volume = volume_directory[current_year]  # same for both ApJ and ApJL - issues run in parallel

volumes = range(start_volume-num_volumes+1, start_volume+1)
