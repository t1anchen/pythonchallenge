import string

def decrypt(cipher):
    old_elems = string.ascii_lowercase
    new_elems = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
    mappings = string.maketrans(old_elems, new_elems)
    return string.translate(cipher, mappings)


def solution():
    return decrypt('map')
