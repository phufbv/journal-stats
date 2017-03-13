from unittest import TestCase
from article import Article


class ArticleTests(TestCase):


    def setUp(self):
    	test_string = 'DatesReceived 2016 November 21Accepted 2017 January 8Published2017 February 3'
        self.article = Article(test_string)


    def test_article_stores_dates(self):
        expectedReceivedDate = '2016 November 21'
    	expectedAcceptedDate = '2017 January 8'

        dates = self.article.get_dates()

        self.assertEqual(expectedReceivedDate, dates[0])
        self.assertEqual(expectedAcceptedDate, dates[1])


    def test_article_calculates_date_difference(self):
        expectedDaysDifference = 48

        daysDifference = self.article.get_dates()[2]

    	self.assertEqual(expectedDaysDifference, daysDifference)

    def test_article_stores_acceptance_year(self):
        expectedYear = int('2017')

        self.assertEqual(expectedYear, self.article.year)


if __name__ == '__main__':
    main()
