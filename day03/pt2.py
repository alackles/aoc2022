import re

numsum = 0

def unicode_to_int(c):
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    for i in range(0, len(lines), 3):
        group = [set(line) for line in lines[i:i+3]]
        dupl = (group[0].intersection(group[1])).intersection(group[2]).pop()
        numsum += unicode_to_int(dupl)

print(numsum)