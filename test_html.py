from unittest import TestCase
import html


class HtmlTests(TestCase):


    def setUp(self):
        self.base_url = "http://iopscience.iop.org/article/10.3847/"

        self.test_vol = 835
        self.test_iss = 1
        self.test_num = 3


    def test_html_builds_apj_url(self):
        #if
        expectedUrl = self.base_url + "1538-4357/835/1/3"

        #when
        url = html.build_url("ApJ", self.test_vol, self.test_iss, self.test_num)

        #then
        self.assertEqual(expectedUrl, url)


    def test_html_builds_apjl_url(self):
        #if
        expectedUrl = self.base_url + "2041-8213/835/1/L3"

        #when
        url = html.build_url("ApJL", self.test_vol, self.test_iss, self.test_num)

        #then
        self.assertEqual(expectedUrl, url)


    def test_html_builds_correct_url_before_vol_833(self):
        #if
        test_vol = 831
        expectedUrl = self.base_url + "2041-8205/831/1/L3"

        #when
        url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

        #then
        self.assertEqual(expectedUrl, url)


    def test_html_builds_correct_url_for_vol_833(self):
        #if
        test_vol = 833
        expectedUrl = self.base_url + "2041-8205/833/1/L3"

        #when
        url = html.build_url("ApJL", test_vol, self.test_iss, self.test_num)

        #then
        self.assertEqual(expectedUrl, url)


if __name__ == '__main__':
    main()
