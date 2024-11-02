import unittest
import urllib2
import requests
import logging
import re
import urllib
import os
import os.path
import Image
import ImageDraw
import webbrowser

# Default is warning, it's to suppress requests INFO log
logging.basicConfig(format="%(message)s")


def solution():
    url = "http://www.pythonchallenge.com/pc/return/good.html"
    html = requests.get(url, auth=("huge", "file")).text
    first_array = map(
        int,
        re.sub(r"\n", "", re.findall(r"first:\n([0-9,\n]+)\n\n", html)[0]).split(","),
    )
    second_array = map(
        int,
        re.sub(r"\n", "", re.findall(r"second:\n([0-9,\n]+)\n\n", html)[0]).split(","),
    )
    image = Image.new("1", (500, 500), 1)  # as max(first_array, second_array) < 500
    draw = ImageDraw.Draw(image)
    draw.line(zip(first_array[0::2], first_array[1::2]))
    draw.line(zip(second_array[0::2], second_array[1::2]))
    image.save("bull.png")
    return "bull"  # if it's cow, url response will return "hmm, it's a male"


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.prefix = "http://www.pythonchallenge.com/pc/return/"
        self.suffix = ".html"

    def tearDown(self):
        png_path = os.path.join("bull.png")
        if os.path.exists(png_path):
            os.remove(png_path)

    def test_solution(self):
        actual = solution()
        expected = "bull"
        cred = ("huge", "file")
        self.assertEquals(actual, expected)
        origin_url = "".join([self.prefix, "bull", self.suffix])
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
            logging.warn("Level 10 is %s with %s" % (r.url, cred))
        else:
            logging.warn("Level 10 is %s with %s" % (origin_url, cred))


if __name__ == "__main__":
    unittest.main(failfast=True)
