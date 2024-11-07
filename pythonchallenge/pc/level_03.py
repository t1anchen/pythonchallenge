import re


def solution(data: str) -> str:
    pattern = r"[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]"
    return "".join(x[4] for x in re.findall(pattern, data))
    # linkedlist
