from datetime import datetime


class Article:

	def __init__(self, date_string):
		self.__find_received_date(date_string)
		self.__find_accepted_date(date_string)
		self.__find_difference()


	def __find_received_date(self, date_string):
		start = date_string.find("Received ") + 9
		end = date_string.find("Accepted")
		    
		self.__received_date = date_string[start:end]


	def __find_accepted_date(self, date_string):
		start = date_string.find("Accepted ") + 9
		end = date_string.find("Published")
		    
		self.__accepted_date = date_string[start:end]

		self.year = int(self.__accepted_date[0:4])


	def __find_difference(self):
		d1 = datetime.strptime(self.__received_date, "%Y %B %d")
		d2 = datetime.strptime(self.__accepted_date, "%Y %B %d")
		    
		self.__date_difference = abs((d2 - d1).days)


	def get_dates(self):
		dates = [self.__received_date, self.__accepted_date, self.__date_difference]

		return dates
