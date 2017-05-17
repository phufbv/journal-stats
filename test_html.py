from unittest import TestCase
import html


class HtmlTests(TestCase):


    def setUp(self):
        self.base_url = "http://iopscience.iop.org/article/10.3847/"

        self.test_vol = 835
        self.test_iss = 1
        self.test_num = 3


    def test_can_detect_start_volume(self):
        self.assertTrue(False)


    def test_html_builds_apj_url(self):
        journal = "ApJ"
        expectedUrl = self.base_url + "1538-4357/835/1/3"

        url = html.build_url(journal, self.test_vol, self.test_iss, self.test_num)

        self.assertEqual(expectedUrl, url)


    def test_html_builds_apjl_url(self):
        journal = "ApJL"
        expectedUrl = self.base_url + "2041-8213/835/1/L3"

        url = html.build_url(journal, self.test_vol, self.test_iss, self.test_num)

        self.assertEqual(expectedUrl, url)


    def test_html_builds_correct_url_before_vol_833(self):
        test_vol = 831
        expectedUrl = self.base_url + "2041-8205/831/1/L3"

        url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

        self.assertEqual(expectedUrl, url)


    def test_html_builds_correct_url_for_vol_833(self):
        test_vol = 833
        expectedUrl = self.base_url + "2041-8205/833/1/L3"

        url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

        self.assertEqual(expectedUrl, url)


    def test_html_extracts_correct_div_from_html_page(self):
        expectedDateString = 'DatesReceived2016 November 21Accepted2017 January 8Published2017 February 3'

        dateString = html.get_date_div("http://iopscience.iop.org/article/10.3847/1538-4357/836/1/1")

        self.assertEqual(expectedDateString, dateString)


if __name__ == '__main__':
    main()
