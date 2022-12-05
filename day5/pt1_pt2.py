import re 

def chunk(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def read_crates(crates, width=4):
    crates = crates.replace('[',' ').replace(']',' ').split('\n')
    num_stacks = int(crates.pop().split()[-1])
    crates = [chunk(crate, width) for crate in crates]
    crates.reverse()
    stacks = [[] for _ in range(num_stacks)]
    for i in range(num_stacks):
        for layer in crates:
            if layer[i].strip():
                stacks[i].append(layer[i].strip())
    return stacks

def read_directions(directions):
    directions = directions.split('\n')
    return [re.findall(r'\d+', dir) for dir in directions]

def move_crates(stacks, dirs, cratemover9001=True):
    for dir in dirs:
        n, start, end = [int(x) for x in dir]
        if cratemover9001:
            stacks[end-1] += stacks[start-1][-n:]
            del stacks[start-1][-n:]
        else:
            for _ in range(n):
                stacks[end-1].append(stacks[start-1].pop())

def get_top(stacks):
    print("".join([stack[-1] for stack in stacks]))
        

with open("input.txt") as f:
    crates, directions = f.read().split('\n\n')
    stacks = read_crates(crates)
    dirs = read_directions(directions)

move_crates(stacks, dirs)
get_top(stacks)