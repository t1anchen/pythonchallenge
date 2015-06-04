import unittest
import requests
import logging
import re
import pickle


# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution():
    url = "http://www.pythonchallenge.com/pc/def/banner.p"
    banner = pickle.loads(requests.get(url).text)
    ret = []
    for g in banner:
        line = ''
        for c, count_c in g:
            line += c * count_c
        ret.append(line)
    return ret


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"

    def test_solution(self):
        actual = solution()
        # It would be identified by pep8, but this is ascii art, who cares!
        expected = ['                                                                                               ',
 '              #####                                                                      ##### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '               ####                                                                       #### ',
 '      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### ',
 '   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### ',
 '  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### ',
 ' ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### ',
 ' ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### ',
 '####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### ',
 '####           ####     ####   ##########    ####     ####  ####     #### ##############  #### ',
 '####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### ',
 '####           ####     #### ####     ###    ####     ####  ####     #### ####            #### ',
 ' ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### ',
 '  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### ',
 '   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### ',
 '      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######',
 '                                                                                               ']
        self.assertEquals(actual, expected)
        origin_url = ''.join([self.prefix, 'channel', self.suffix])
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
