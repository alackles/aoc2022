class CPU:

    def __init__(self, start, stop, step):
        self.clock = 1
        self.X = 1
        self.sprite = [self.X-1, self.X, self.X+1]
        self.signals = range(start, stop+step, step)
        self.sigsum = 0
        self.crt = [" " for _ in range(start + stop)]
    
    def is_signal(self):
        return self.clock in self.signals
    
    def move_sprite(self):
        self.sprite = [self.X-1, self.X, self.X + 1]
    
    def add_signal(self):
        if self.is_signal():
            self.sigsum += self.X * self.clock
    
    def draw_pixel(self):
        if (self.clock - 1) % 40 in self.sprite:
            self.crt[self.clock-1] = "#"

    def exec(self, cmd):
        match cmd.split():
            case ["noop"]:
                self.draw_pixel()
                self.clock += 1
                self.add_signal()
            case ["addx", V]:
                self.draw_pixel()
                self.clock += 1
                self.add_signal()
                self.draw_pixel()
                self.clock += 1
                self.X += int(V)
                self.add_signal()
                self.move_sprite()

    def display(self, width):
        crt = [self.crt[i:i+width] for i in range(0, len(self.crt), width)]
        for line in crt:
            print("".join(line))

with open("input.txt") as f:
    cpu = CPU(20, 220, 40)
    for cmd in f.readlines():
        cpu.exec(cmd.strip())

cpu.display(40)

    


