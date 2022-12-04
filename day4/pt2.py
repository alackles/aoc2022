def overlapping(a1, a2, b1, b2):
    overlaps = (a1 <= b1 <= a2 <= b2) or (b1 <= a1 <= b2 <= a2)
    contains = (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2)
    return overlaps or contains

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace('-',',')
        a1, a2, b1, b2 = [int(x) for x in line.strip().split(',')]
        if overlapping(a1, a2, b1, b2):
            total += 1

print(total)
        