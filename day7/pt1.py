import re

class Directory:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.dirs = []
        self.size = 0

def is_cd(cmd):
    return re.match(r"\$ cd ", cmd)

def is_dir(cmd):
    return re.match(r"dir ", cmd)

def is_file(cmd):
    return re.match(r"\d+", cmd)

def append_dir(a, b):
    return a + "/" + b if a != "/" and b != "/" else b # really messy way to make the files print out nicely

def parse_cmd(filename):
    filestruct = {}
    current_dir = None
    with open(filename) as terminal:
        for cmd in terminal:

            # Grabbing the command
            cmd = cmd.strip()               
            fname = cmd.split()[-1]       

            # Changing to a new directory  
            if is_cd(cmd):
                prev_dir = current_dir
                if fname == "..":
                    current_dir = filestruct[current_dir].parent
                else: 
                    current_dir = append_dir(current_dir, fname)
                    filestruct.setdefault(current_dir, Directory(current_dir))
                    filestruct[current_dir].parent = prev_dir
            
            # Discovering a new directory
            elif is_dir(cmd):
                filestruct[current_dir].dirs.append(append_dir(current_dir, fname))
            
            # Reading a file size and adding to all previous directories
            elif is_file(cmd):
                filesize = int(cmd.split()[0])
                filestruct[current_dir].size += filesize
                par = filestruct[current_dir].parent
                while par is not None:
                    filestruct[par].size += filesize
                    par = filestruct[par].parent

    return filestruct


def find_size(filestruct, maxsize=100000):
    full_sum = 0
    for v in filestruct.values():
        if v.size < maxsize:
            full_sum += v.size
    return full_sum

filestruct = parse_cmd("input.txt")
print(find_size(filestruct))