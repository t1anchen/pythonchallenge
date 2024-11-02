import unittest
import urllib2
import requests
import logging
import re
import urllib
import os
import os.path

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format="%(message)s")


def next_seq_item(current_item):
    last_digit = current_item[0]
    next_item = ""
    last_digit_count = 0
    for digit in current_item:
        if digit == last_digit:
            last_digit_count += 1
        else:
            next_item += str(last_digit_count)
            next_item += last_digit
            last_digit = digit
            last_digit_count = 1
    next_item += str(last_digit_count)
    next_item += last_digit
    return next_item


def solution():
    last_item = "1"
    for i in range(30):
        last_item = next_seq_item(last_item)
    return str(len(last_item))


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/return/"
        self.suffix = ".html"

    def test_solution(self):
        actual = solution()
        expected = "5808"
        cred = ("huge", "file")
        self.assertEquals(actual, expected)
        origin_url = "".join([self.prefix, "5808", self.suffix])
        try:
            r = requests.get(origin_url, auth=cred)
        except:
            raise
        self.assertTrue(r.ok)
        next_entry = [
            re.sub(r"(.*)URL=(.*)\.html\"\>", r"\2", line)
            for line in r.iter_lines()
            if re.match(r".*URL.*", line)
        ]
        r.close()
        if len(next_entry) != 0:
            r = requests.get(
                "".join([self.prefix, next_entry[0], self.suffix], auth=expected)
            )
            logging.warn("Level 11 is %s with %s" % (r.url, cred))
        else:
            logging.warn("Level 11 is %s with %s" % (origin_url, cred))


if __name__ == "__main__":
    unittest.main(failfast=True)
