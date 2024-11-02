'''Level 17: romance
http://www.pythonchallenge.com/pc/return/romance.html
'''

import requests
import re
from collections import deque
from urllib.parse import unquote_to_bytes
import bz2

def solution():
    '''
    1. cookies.jpg
    2. http://www.pythonchallenge.com/pc/return/cookies.html -> chocolate
    3. http://www.pythonchallenge.com/pc/return/chocolate.html -> play
    4. http://www.pythonchallenge.com/pc/return/play.html -> go back
    5. image left-down corner -> level 4
    6. (level 4, cookies) -> you should have followed busynothing
    7. s/nothing/busynothing/g
    8. Find all numbers and collect cookie values
    9. unquote_plus cookies values with bz2 decompressed
    '''
    n = '12345'
    prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    cookies = []
    with requests.Session() as s:
        while len(re.findall('\d+', n)) > 0:
            res = s.get(prefix, params={'busynothing': n})
            numbers = re.findall('\d+', res.text)
            print(res.text, numbers)
            n = next(iter(deque(numbers, maxlen=1)), '')
            cookies += s.cookies.values()
    quoted_hint_with_plus = ''.join(cookies)

    # In Python2, simply urllib.unquote_plus() is enough
    # As in Python3, all strings are unicoded
    # We need to replace plus mark with space
    # (https://hg.python.org/cpython/file/2.7/Lib/urllib.py#l1251)
    # and convert it to bytes-object and unquoted
    quoted_hint_bytes = quoted_hint_with_plus.replace('+', ' ').encode('ascii')
    hint = bz2.decompress(unquote_to_bytes(quoted_hint_bytes)).decode()
    # hint: is it the 26th already? call his father and inform him that "the
    # flowers are on their way". he\'ll understand.
    return 'balloons'
