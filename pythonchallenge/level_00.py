import unittest
import requests
import logging
import re

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution():
    return str(2**38)


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"

    def test_solution(self):
        try:
            r = requests.get(''.join([self.prefix, solution(), self.suffix]))
        except:
            raise
        self.assertTrue(r.ok)
        next_entry = [re.sub(r'(.*)URL=(.*)\.html\"\>', r'\2', line)
                      for line in r.iter_lines() if re.match(r'.*URL.*', line)]
        if len(next_entry) != 0:
            r.close()
            r = requests.get(
                ''.join([self.prefix, next_entry[0], self.suffix]))
            logging.warn('Level 01 is %s' % r.url)


if __name__ == "__main__":
    unittest.main(failfast=True)
