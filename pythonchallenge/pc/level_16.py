'''Level 16: Mozart
'''

from PIL import Image
from PIL import ImageChops
import requests
from io import BytesIO # use cStringIO.StringIO if python2

def solution():
    '''Get pink segments into straight
    GIF image uses Palettes for colors (https://en.wikipedia.org/wiki/GIF#Palettes)
    '''
    PURPLE_CODE = 195
    res = requests.get('http://www.pythonchallenge.com/pc/return/mozart.gif', auth=('huge', 'file'))
    img = Image.open(BytesIO(res.content))
    x_max, y_max = img.size
    for y in range(y_max):
        box = 0, y, x_max, y+1
        row_pixels = img.crop(box)
        pixels_data = row_pixels.tobytes()
        purple_idx = pixels_data.index(PURPLE_CODE)
        row_pixels = ImageChops.offset(row_pixels, -purple_idx)
        img.paste(row_pixels, box)
    img.show() # display 'romance'

    return 'romance'
