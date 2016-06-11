'''Level 14: ITALY
'''

from PIL import Image
import requests
from io import BytesIO # use cStringIO.StringIO if python2
from itertools import cycle, tee, islice
from operator import add

def fibs():
    '''Fibonacci Stream
    It comes from http://joelgrus.com/2015/07/07/haskell-style-fibonacci-in-python/
    '''
    yield 1
    yield 1
    fibs1, fibs2 = tee(fibs())
    yield from map(add, fibs1, islice(fibs2, 1, None))

def solution():
    '''Twist line into square
    '''
    res = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=('huge', 'file'))
    img = Image.open(BytesIO(res.content))
    delta = cycle([0, -1, -1, -2])
