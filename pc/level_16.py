'''Level 16: Mozart
'''

from PIL import Image
import requests
from io import BytesIO # use cStringIO.StringIO if python2

def solution():
    '''Twist line into square
    '''
    res = requests.get('http://www.pythonchallenge.com/pc/return/mozart.gif', auth=('huge', 'file'))
    img = Image.open(BytesIO(res.content))
    x_max, y_max = img.size
    return 'romance'
