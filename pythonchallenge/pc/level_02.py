import string


def solution(haystack: str) -> str:
    return "".join(c for c in haystack if c in string.ascii_letters)
    # equality
