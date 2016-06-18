'''Level 14: ITALY
'''

from PIL import Image
import requests
from io import BytesIO # use cStringIO.StringIO if python2
from itertools import cycle

def solution():
    '''Twist line into square
    '''
    res = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=('huge', 'file'))
    img = Image.open(BytesIO(res.content))
    delta = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    img_new = Image.new(img.mode, (100, 100)) # Create new image by original mode of the image with 100x100
    x, y, x_origin = -1, 0, 0
    doubled_steps = 200
    while doubled_steps // 2 > 0:
        x_delta, y_delta = next(delta)
        for i in range(doubled_steps // 2):
            x, y = x + x_delta, y + y_delta
            img_new.putpixel((x, y), img.getpixel((x_origin, 0)))
            x_origin += 1
        doubled_steps -= 1
    img_new.show() # it's a lovely kitty
    return 'cat'
