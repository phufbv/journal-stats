from unittest import TestCase
import html


class HtmlTests(TestCase):


	def setUp(self):
		self.base_url = "http://iopscience.iop.org/article/10.3847/"

		self.test_vol = 835
		self.test_iss = 1
		self.test_num = 3


	def test_can_detect_start_volume_in_current_year(self):
		yearToCover = 2017
		expectedStartVol = 854

		(start_volume, previous_year) = html.detect_start_volume()

		self.assertEqual(yearToCover, previous_year)
		self.assertEqual(expectedStartVol, start_volume)


	def test_html_builds_apj_url(self):
		#Functionally replaced by test_html_extracts_article_urls_from_contents_page
		journal = "ApJ"
		expectedUrl = self.base_url + "1538-4357/835/1/3"

		url = html.build_url(journal, self.test_vol, self.test_iss, self.test_num)

		self.assertEqual(expectedUrl, url)


	def test_html_builds_apjl_url(self):
		#Functionally replaced by test_html_extracts_article_urls_from_contents_page
		journal = "ApJL"
		expectedUrl = self.base_url + "2041-8213/835/1/L3"

		url = html.build_url(journal, self.test_vol, self.test_iss, self.test_num)

		self.assertEqual(expectedUrl, url)


	def test_html_builds_correct_url_before_vol_833(self):
		#Functionally replaced by test_html_extracts_article_urls_from_contents_page
		test_vol = 831
		expectedUrl = self.base_url + "2041-8205/831/1/L3"

		url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

		self.assertEqual(expectedUrl, url)


	def test_html_builds_correct_url_for_vol_833(self):
		#Functionally replaced by test_html_extracts_article_urls_from_contents_page
		test_vol = 833
		expectedUrl = self.base_url + "2041-8205/833/1/L3"

		url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

		self.assertEqual(expectedUrl, url)


	def test_html_extracts_correct_div_from_html_page(self):
		expectedDateString = 'DatesReceived2016 November 21Accepted2017 January 8Published2017 February 3'

		dateString = html.get_date_div("http://iopscience.iop.org/article/10.3847/1538-4357/836/1/1")

		self.assertEqual(expectedDateString, dateString)


	def test_html_extracts_article_urls_from_contents_page_apj(self):
		journal = "ApJ"
		volume = 836
		issue = 2

		expectedArticleUrls = ["/article/10.3847/1538-4357/aa5be8","/article/10.3847/1538-4357/aa5b8b","/article/10.3847/1538-4357/aa5b88","/article/10.3847/1538-4357/836/2/152","/article/10.3847/1538-4357/836/2/153"]
		#URLs of first 5 articles in this issue

		articleUrls = html.get_article_urls(journal, volume, issue)
		#URLs of all articles in the issue

		self.assertEqual(expectedArticleUrls, articleUrls[:4])


	# def test_html_extracts_article_urls_from_contents_page_apjl(self):
	# 	journal = "ApJ"
	# 	volume = 836
	# 	issue = 2

	# 	expectedArticleUrls = ["/article/10.3847/2041-8213/836/2/L17","/article/10.3847/2041-8213/aa5dab","/article/10.3847/2041-8213/aa5cb0","/article/10.3847/2041-8213/aa5eb0","/article/10.3847/2041-8213/aa5dee"]
	# 	#URLs of first 5 articles in this issue

	# 	articleUrls = html.get_article_urls(journal, volume, issue)
	# 	#URLs of all articles in the issue

	# 	self.assertEqual(expectedArticleUrls, articleUrls[:4])


if __name__ == '__main__':
	main()
