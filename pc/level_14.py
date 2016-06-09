from PIL import Image
import requests
from io import BytesIO # use cStringIO.StringIO if python2
from itertools import cycle, tee, islice
from operator import add

# it comes from http://joelgrus.com/2015/07/07/haskell-style-fibonacci-in-python/
def fibs():
    yield 1
    yield 1
    fibs1, fibs2 = tee(fibs())
    yield from map(add, fibs1, islice(fibs2, 1, None))

def solution():
    res = requests.get('http://www.pythonchallenge.com/pc/return/wire.jpg', auth=('huge', 'file'))
    img = Image.open(BytesIO(res.content))
    delta = cycle([0, -1, -1, -2])
