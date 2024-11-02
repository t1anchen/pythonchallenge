import unittest
import requests
import logging
import re
import string


# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution(data):
    return filter(lambda x: x in string.letters, data)


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"
        self.src_url = "http://www.pythonchallenge.com/pc/def/ocr.html"

    def test_solution(self):
        actual = ''
        r = requests.get(self.src_url)
        actual = solution(re.findall('<!--[^>]*-->', r.text)[1])
        expected = 'equality'
        self.assertEquals(actual, expected)
        r.close()
        origin_url = ''.join([self.prefix, actual, self.suffix])
        try:
            r = requests.get(origin_url)
        except:
            raise
        self.assertTrue(r.ok)
        next_entry = [re.sub(r'(.*)URL=(.*)\.html\"\>', r'\2', line)
                      for line in r.iter_lines() if re.match(r'.*URL.*', line)]
        r.close()
        if len(next_entry) != 0:
            r = requests.get(
                ''.join([self.prefix, next_entry[0], self.suffix]))
            logging.warn('Level 03 is %s' % r.url)
        else:
            logging.warn('Level 03 is %s' % origin_url)


if __name__ == "__main__":
    unittest.main(failfast=True)
