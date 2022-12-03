import re

numsum = 0

def unicode_to_int(c):
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        unique = "".join(["".join(set(s)) for s in group])
        full = "".join(sorted(unique))
        dupl = re.search(r"([a-zA-z])\1\1", full).groups()[0]
        numsum += unicode_to_int(dupl)

print(numsum)