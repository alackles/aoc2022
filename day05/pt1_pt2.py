import re 


def chunk(s, n):
    # Splits a string s into chunks of length n
    return [s[i:i+n] for i in range(0, len(s), n)]

def read_crates(crates, width=4):
    # Parse crates section of input
    crates = crates.replace('[',' ').replace(']',' ').split('\n')       # turn all brackets into more whitespace
    num_stacks = int(crates.pop().split()[-1])                          # take off the last row (numbers) & return the number of stacks
    crates = [chunk(crate, width) for crate in crates]                  # create the rows of crates, top to bottom
    crates.reverse()                                                    # flip the rows, so now we can read bottom to top
    stacks = [[] for _ in range(num_stacks)]                            # initialize num_stacks empty stacks
    for i in range(num_stacks):                                         # loop through first stack, bottom to top; then second stack, bottom to top, etc
        for layer in crates:
            if layer[i].strip():
                stacks[i].append(layer[i].strip())                      # add to the stack whenever there's a letter
    return stacks                                                       

def read_directions(directions):
    # Parse directions section of input
    directions = directions.split('\n')
    return [re.findall(r'\d+', dir) for dir in directions]

def move_crates(stacks, dirs, cratemover9001=True):
    # Perform the actual movements
    for dir in dirs:
        n, start, end = [int(x) for x in dir]
        if cratemover9001:
            # Part 2
            stacks[end-1] += stacks[start-1][-n:]               # Append the last n elements of the start stack to the end stack
            del stacks[start-1][-n:]                            # Delete the last n elements of the start stack
        else:
            # Part 1
            for _ in range(n):
                stacks[end-1].append(stacks[start-1].pop())     # Pop off the start stack and push onto the end stack

def get_top(stacks):
    # Convert to puzzle input format
    print("".join([stack[-1] for stack in stacks]))             # Gets the last element of each stack
        

# Read file
with open("input.txt") as f:
    crates, directions = f.read().split('\n\n')

stacks = read_crates(crates)
dirs = read_directions(directions)
move_crates(stacks, dirs) # add cratemover9001=False as optional parameter to do part 1
get_top(stacks)