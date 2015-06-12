import unittest
import urllib2
import requests
import logging
import re
import urllib
import os
import os.path
import bz2

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution():
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    return (bz2.decompress(un), bz2.decompress(pw))


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/return/"
        self.suffix = ".html"

    def test_solution(self):
        actual = solution()
        # It would be identified by pep8, but this is ascii art, who cares!
        expected = ('huge', 'file')
        self.assertEquals(actual, expected)
        # Trick: hockey is consist of letters of oxygen
        origin_url = ''.join([self.prefix, 'good', self.suffix])
        try:
            r = requests.get(origin_url, auth=expected)
        except:
            raise
        self.assertTrue(r.ok)
        next_entry = [re.sub(r'(.*)URL=(.*)\.html\"\>', r'\2', line)
                      for line in r.iter_lines() if re.match(r'.*URL.*', line)]
        r.close()
        if len(next_entry) != 0:
            r = requests.get(
                ''.join([self.prefix, next_entry[0], self.suffix], auth=expected))
            logging.warn('Level 06 is %s with %s' % (r.url, expected))
        else:
            logging.warn('Level 06 is %s with %s' % (origin_url, expected))


if __name__ == "__main__":
    unittest.main(failfast=True)
