import unittest
import requests
import logging
import re
import zipfile
import urllib


# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format='%(message)s')


def solution():
    url = "http://www.pythonchallenge.com/pc/def/channel.zip"
    urllib.urlretrieve(url, "/tmp/channel.zip")
    zip_file = zipfile.ZipFile("/tmp/channel.zip")
    zip_file_comments = []
    member_name = "90052.txt"
    while True:
        zip_info = zip_file.getinfo(member_name)
        with zip_file.open(member_name) as member_stream:
            number = re.findall(r'\d+$', member_stream.read())
        zip_file_comments.append(zip_info.comment)
        if number:
            member_name = '%s.txt' % number[0]
        else:
            break
    return ''.join(zip_file_comments)


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/def/"
        self.suffix = ".html"

    def test_solution(self):
        actual = solution()
        # It would be identified by pep8, but this is ascii art, who cares!
        expected = '''****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
'''
        self.assertEquals(actual, expected)
        origin_url = ''.join([self.prefix, 'oxygen', self.suffix])  # Trick: hockey is consist of letters of oxygen
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
