# helper dictionary to translate ABC to RPS
rps_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

shapes = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def rps(player, opp, win=6, draw=3, lose=0):
    paper_rock = player == "Paper" and opp == "Rock"
    rock_scissors = player == "Rock" and opp == "Scissors"
    scissors_paper = player == "Scissors" and opp == "Paper"
    if paper_rock or rock_scissors or scissors_paper:
        return win
    elif player == opp:
        return draw
    else: 
        return lose

score = 0

with open("input.txt") as f:
    for line in f.readlines():
        opp, player = [rps_dict[x] for x in line.strip().split()]
        score += rps(player, opp) + shapes[player]

with open("output.txt", "w") as f:
    f.write(str(score))