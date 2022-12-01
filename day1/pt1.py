
max_cals = 0

with open("input.txt") as f:
    cals = 0
    for line in f.readlines():
        if line == "\n":
            if cals > max_cals:
                max_cals = cals
            cals = 0
        else:
            cals += int(line.strip())

with open("output.txt", "w") as f:
    f.write(str(max_cals))
        