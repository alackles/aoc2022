import re

numsum = 0

def unicode_to_int(c):
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        n = int(len(line)/2)
        unique = "".join(set(line[:n])) + "".join(set(line[n:]))
        full = "".join(sorted(unique))
        dupl = re.search(r"([a-zA-z])\1", full).groups()[0]
        numsum += unicode_to_int(dupl)

print(numsum)