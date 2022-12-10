import math

class Knot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def right_of(self, other):
        return self.x > other.x
    
    def left_of(self, other):
        return self.x < other.x
    
    def top_of(self, other):
        return self.y > other.y
    
    def bottom_of(self, other):
        return self.y < other.y

class Rope:
    def __init__(self, x, y):
        self.head = Knot(x,y)
        self.tail = Knot(x,y)
        self.visited = {(self.tail.x, self.tail.y)}
    
    def __repr__(self):
        return f"Head: ({self.head.x}, {self.head.y})  Tail: ({self.tail.x}, {self.tail.y})"
    
    def distance(self):
        return math.sqrt((self.head.x - self.tail.x)**2 + (self.head.y - self.tail.y)**2)
    
    def is_adjacent(self):
        return self.distance() <= math.sqrt(2)
    
    def move_tail(self):
        if self.is_adjacent():
            return
        if self.head.right_of(self.tail):
            self.tail.x += 1
        elif self.head.left_of(self.tail):
            self.tail.x -= 1
        if self.head.top_of(self.tail):
            self.tail.y += 1
        elif self.head.bottom_of(self.tail):
            self.tail.y -= 1
        self.visited.add((self.tail.x, self.tail.y))
        

    def move_head(self, dir):
        match dir:
            case "R":
                self.head.x += 1
            case "L":
                self.head.x -= 1
            case "U":
                self.head.y += 1
            case "D":
                self.head.y -= 1

with open("input.txt") as f:
    ropechain = [Rope(0, 0) for _ in range(9)]
    for line in f.readlines():
        dir, dist = line.strip().split()
        for _ in range(int(dist)):
            ropechain[0].move_head(dir)
            ropechain[0].move_tail()
            
            for i in range(1, len(ropechain)):
                # move the head of the next rope chain to the tail of the last rope chain
                ropechain[i].head.x = ropechain[i-1].tail.x
                ropechain[i].head.y = ropechain[i-1].tail.y
                # move the rope's tail accordingly
                ropechain[i].move_tail()
            

print(len(ropechain[-1].visited))


