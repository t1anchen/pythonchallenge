import unittest
import requests
import logging
import re
import urllib
import os
import os.path
import Image  # requires PIL or Pillow

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution():
    url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
    urllib.urlretrieve(url, "oxygen.png")
    image_file = Image.open("oxygen.png")
    the_grey_panel = [
        image_file.getpixel((i, 43))[0] for i in xrange(0, 609, 7)]
    hint = ''.join(map(chr, the_grey_panel))
    logging.warn(hint)
    return ''.join(map(lambda x: chr(int(x)), re.findall(r'\d{3}', hint)))


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"

    def tearDown(self):
        zip_path = "oxygen.png"
        if os.path.exists(zip_path):
            os.remove(zip_path)

    def test_solution(self):
        actual = solution()
        # It would be identified by pep8, but this is ascii art, who cares!
        expected = 'integrity'
        self.assertEquals(actual, expected)
        # Trick: hockey is consist of letters of oxygen
        origin_url = ''.join([self.prefix, 'integrity', self.suffix])
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
            logging.warn('Level 06 is %s' % r.url)
        else:
            logging.warn('Level 06 is %s' % origin_url)


if __name__ == "__main__":
    unittest.main(failfast=True)
