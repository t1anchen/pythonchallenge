import requests
import re
from collections import deque

def solution():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    n = '12345'
    while len(re.findall('\d+', n)) > 0:
        print(n)
        res = requests.get(url, params={'nothing': n})
        numbers = re.findall('\d+', res.text)
        if re.search('[Dd]ivide', res.text):
            n = str(int(n) // 2)
        elif len(numbers) > 1:
            n = deque(numbers, maxlen=1).pop()
        elif len(numbers) > 0:
            n = numbers[0]
        elif re.search('html', res.text):
            n = re.sub(r'(.+)\.html', r'\1', res.text)
    return n # 'peak'
