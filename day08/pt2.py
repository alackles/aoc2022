import numpy as np 

class Tree:
    def __init__(self, h):
        self.h = h
        self.viz = None
        self.left = 0
        self.right = 0
        self.down = 0
        self.up = 0
        self.scenic = 0
    
    def __repr__(self):
        return f"({self.h}, {self.viz})"
    
    def __str__(self):
        return f"({self.h}, {self.viz})"
    
    def __ge__(self, other):
        return self.h >= other.h

class Forest:
    def __init__(self, table):
        self.table = table
        self.nrow = len(table)
        self.ncol = len(table[0])
        for i, row in enumerate(self.table):
            for j, col in enumerate(row):
                col.viz = (i == 0 or i == self.nrow-1) or (j == 0 or j == self.ncol-1) # set initial outer visualization
    
    def set_visible(self, row, col):
        tree = self.table[row][col]
        # check left
        left = True
        for j in range(col-1, -1, -1):
            tree.left += 1
            if self.table[row][j] >= tree:
                left = False
                break
        right = True
        for j in range(col+1, self.ncol):
            tree.right += 1
            if self.table[row][j] >= tree:
                right = False
                break
        up = True
        for i in range(row-1, -1, -1):
            tree.up += 1
            if self.table[i][col] >= tree:
                up = False
                break
        down = True
        for i in range(row+1, self.nrow):
            tree.down += 1
            if self.table[i][col] >= tree:
                down = False
                break
        tree.scenic = tree.left * tree.right * tree.up * tree.down
        tree.viz = left or right or up or down
    
    def set_all_visible(self):
        for i in range(1, self.nrow-1):
            for j in range(1, self.ncol-1):
                self.set_visible(i, j)
    
    def get_visible(self):
        ct = 0
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.table[i][j].viz:
                    ct += 1
        return ct
    
    def max_scenic(self):
        scenicmax = 0
        for i in range(1, self.nrow-1):
            for j in range(1, self.ncol-1):
                if self.table[i][j].scenic > scenicmax:
                    scenicmax = self.table[i][j].scenic
        return scenicmax

        
    def display(self):
        for i in self.table:
            print(i)

with open("input.txt") as f:
    forest = Forest([[Tree(x) for x in line.strip()] for line in f])

forest.set_all_visible()
print(forest.max_scenic())