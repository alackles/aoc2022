import re

class Group:

    def __init__(self, group):
        self.group = group

    def do_round(self):
        for monkey in self.group:
            while monkey.q:
                old = monkey.q.pop(0)
                monkey.count += 1
                new = monkey.oper(old)
                new = new//3
                dest = monkey.dest(new)
                self.group[dest].q.append(new)
    
    def monkey_business(self):
        top = ([monkey.count for monkey in sorted(self.group)])
        return top[0]*top[1]
    
    def __repr__(self):
        return str(self.group)

        

class Monkey:
    def __init__(self, id, q):
        self.id = id
        self.q = q
        self.count = 0

    def __lt__(self, other):
        return self.count < other.count
    
    def __repr__(self):
        return f"(id: {self.id}, q: {self.q}, ct: {self.count})"
    
    def set(self, op, test):
        self.op, self.num = op.lstrip("new = old ").split()
        self.mod, self.tdest, self.fdest = test
    
    def oper(self, x):
        match self.op:
            case "+":
                if self.num.isdigit():
                    return x + int(self.num)
                else:
                    return x + x
            case "*":
                if self.num.isdigit():
                    return x * int(self.num)
                else:
                    return x * x    
    
    def dest(self, x):
        return self.fdest if x % self.mod else self.tdest

def parseblock(block):
    idline, qline, opline, modline, tline, fline = [line.strip() for line in block.split("\n")]
    id = idline.strip(":").split()[-1] 
    q = [int(x) for x in qline.split(":")[-1].strip().split(",")]
    op = opline.split(":")[-1]
    mod = re.search(r"\d+", modline).group(0)
    t = re.search(r"\d+", tline).group(0)
    f = re.search(r"\d+", fline).group(0)
    monkey = Monkey(id, q)
    monkey.set(op, [int(mod), int(t), int(f)])
    return monkey

with open("toy.txt") as f:
    group = Group([parseblock(monkey) for monkey in f.read().split("\n\n")])

for _ in range(20):
    group.do_round()

print(group.monkey_business())