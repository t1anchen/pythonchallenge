'''Level 17: romance
http://www.pythonchallenge.com/pc/return/romance.html
'''

import requests
import re
from collections import deque

def solution():
    '''
    1. cookies.jpg
    2. http://www.pythonchallenge.com/pc/return/cookies.html -> chocolate
    3. http://www.pythonchallenge.com/pc/return/chocolate.html -> play
    4. http://www.pythonchallenge.com/pc/return/play.html -> go back
    5. image left-down corner -> level 4
    6. (level 4, cookies) -> you should have followed busynothing
    7. s/nothing/busynothing/g
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
    print(''.join(cookies))
    return 'balloons'
