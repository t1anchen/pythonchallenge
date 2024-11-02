import unittest
import urllib
import requests
import logging
import re
import urllib
import os
import os.path
import Image
import ImageDraw
from StringIO import StringIO

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format="%(message)s")


def solution():
    url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
    r = requests.get(url, auth=("huge", "file"))
    image_file = Image.open(StringIO(r.content))
    new_image = Image.new("RGB", (640, 480), "black")
    new_image_stroke = ImageDraw.Draw(new_image)
    for y in xrange(480):
        for x in xrange(640):
            if y % 2 == 0 and x % 2 == 0 or y % 2 == 1 and x % 2 == 1:
                new_image.putpixel((x, y), image_file.getpixel((x, y)))
    new_image.save("cave_edited.jpg")
    return "evil"


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/return/"
        self.suffix = ".html"

    def tearDown(self):
        os.remove("cave_edited.jpg")

    def test_solution(self):
        actual = solution()
        expected = "evil"
        cred = ("huge", "file")
        self.assertEquals(actual, expected)
        origin_url = "".join([self.prefix, "evil", self.suffix])
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
            logging.warn("Level 12 is %s with %s" % (r.url, cred))
        else:
            logging.warn("Level 12 is %s with %s" % (origin_url, cred))


if __name__ == "__main__":
    unittest.main(failfast=True)
