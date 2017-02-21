# journal-stats
For comparative analysis of academic journal publication data.

  
### Program description ###
This program will go to The Astrophysical Journal website and retrieve the 'Received' and 'Accepted' dates for a sample of articles published in ApJ or ApJL in the previous year, saving them into a spreadsheet.

Inputs: none  
Outputs: .csv file (open in Excel)

### Technical details ###

Assumptions:  
* There are at least 30 articles per issue
* There are 2 issues per volume
* There are 18 volumes per year (1.5 per month, averaged)

The program currently automatically detects the first February volume of the current year (e.g. Volume 836: Number 1, 10 February 2017). It will attempt to load the URLs of the first 30 articles in issue 1 of this volume. It will retrieve the dates for as many of these as possible, before doing the same for issue 1 of the previous volume, and then issue 1 of the volume before that, etc.  

The program will loop through the previous 18 volumes in this manner, corresponding to the previous year, to return the dates for a sample of at least 500 articles (URLs on the ApJ website are not entirely consistent, so the date retrieval may fail for some articles). For at least the last 5 years (2012 - 2016 inclusive), there have been 18 volumes of ApJ per year, each with 2 issues, so it is assumed that this pattern will continue.

The search parameters (number of articles per issue, whether to use issue 1 or 2, and the number of volumes to loop through) are defined in the file 'parameters.py', and can be changed by the user. Whether to sample ApJ or ApJL, and the output file name, are also set here. If the number of volumes is set to more than 18, the program will just continue back through and sample more than a year.
