# helper dictionary to translate ABC to RPS
rps_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

shapes = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

points = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

def rps(opp, key):
# winner : loser
    rules = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper": "Rock"
    }
    if key == "draw":
        return opp
    elif key == "win":
        return rules[rules[opp]]
    else:
        return rules[opp]
    

score = 0

with open("input.txt") as f:
    for line in f.readlines():
        opp, key = [rps_dict[x] for x in line.strip().split()]
        print(rps(opp, key))
        score += shapes[rps(opp, key)] + points[key]

with open("output.txt", "w") as f:
    f.write(str(score))