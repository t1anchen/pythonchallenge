import unittest
import requests
import logging
import re
import string


# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def next_n(prefix, n):
    url_prefix = ''.join([prefix, "linkedlist.php?nothing="])
    addr = ''.join([url_prefix, n])
    logging.warn(addr)
    r = requests.get(addr)
    logging.warn(r.text)
    ns = re.findall('[0-9]+', r.text)
    ret = ''
    if re.search('[Dd]ivide', r.text):
        ret = str(int(n)/2)
    elif len(ns) > 1:
        ret = ns[-1]
    elif len(ns) > 0:
        ret = ns[0]
    elif re.search('html', r.text):
        ret = re.sub(r'(.+)\.html', r'\1', r.text)
    r.close()
    return ret


def solution(prefix, n_0):
    n = n_0
    while True:
        n = next_n(prefix, n)
        try:
            int(n)
        except:
            break
    return n


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"
        self.src_url = "http://www.pythonchallenge.com/pc/def/equality.html"

    def test_solution(self):
        actual = solution(self.prefix, '12345')
        expected = 'peak'
        self.assertEquals(actual, expected)
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
            logging.warn('Level 05 is %s' % r.url)
        else:
            logging.warn('Level 05 is %s' % origin_url)


if __name__ == "__main__":
    unittest.main(failfast=True)
