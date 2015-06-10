import unittest
import requests
import logging
import re
import string

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def decrypt(cipher):
    old_elems = string.ascii_lowercase
    new_elems = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    mappings = string.maketrans(old_elems, new_elems)
    return string.translate(cipher, mappings)


def solution():
    return decrypt('map')


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"

    def test_decrypt(self):
        test_data = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. ''' + \
                    '''rfyrq ufyr amknsrcpq ypc dmp. ''' + \
                    '''bmgle gr gl zw fylb gq glcddgagclr ylb ''' + \
                    '''rfyr'q ufw rfgq rcvr gq qm jmle. ''' + \
                    '''sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. ''' + \
                    '''lmu ynnjw ml rfc spj.'''
        actual = decrypt(test_data)
        expected = '''i hope you didnt translate it by hand. ''' + \
            '''thats what computers are for. ''' + \
            '''doing it in by hand is inefficient and ''' + \
            '''that's why this text is so long. ''' + \
            '''using string.maketrans() is recommended. ''' + \
            '''now apply on the url.'''
        self.assertEquals(actual, expected)

    def test_solution(self):
        origin_url = ''.join([self.prefix, solution(), self.suffix])
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
            logging.warn('Level 02 is %s' % r.url)
        else:
            logging.warn('Level 02 is %s' % origin_url)


if __name__ == "__main__":
    unittest.main(failfast=True)
