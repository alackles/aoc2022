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
        

    def move_head(self, dir, dist):
        for _ in range(dist):
            match dir:
                case "R":
                    self.head.x += 1
                case "L":
                    self.head.x -= 1
                case "U":
                    self.head.y += 1
                case "D":
                    self.head.y -= 1
            self.move_tail()
            self.visited.add((self.tail.x, self.tail.y))


with open("input.txt") as f:
    rope = Rope(0, 0)
    for line in f.readlines():
        dir, dist = line.strip().split()
        rope.move_head(dir, int(dist))

print(len(rope.visited))


