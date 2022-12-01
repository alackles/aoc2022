
max_cals = [0, 0, 0]

with open("input.txt") as f:
    cals = 0
    for line in f.readlines():
        if line == "\n":
            if cals > min(max_cals):
                max_cals[max_cals.index(min(max_cals))] = cals
            cals = 0
        else:
            cals += int(line.strip())

with open("output.txt", "w") as f:
    f.write(str(sum(max_cals)))
        