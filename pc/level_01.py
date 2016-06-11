import string

def decrypt(cipher):
    # cipher: string
    old_elems = string.ascii_lowercase
    new_elems = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    mappings = cipher.maketrans(old_elems, new_elems) # python2: string.maketrans(old_elems, new_elems)
    return cipher.translate(mappings) # python2: string.translate(cipher, mappings)

def solution():
    return decrypt('map')
