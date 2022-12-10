class CPU:

    def __init__(self, start, stop, step):
        self.clock = 1
        self.X = 1
        self.signals = range(start, stop+step, step)
        self.sigsum = 0
    
    def is_signal(self):
        return self.clock in self.signals
    
    def add_signal(self):
        if self.is_signal():
            self.sigsum += self.X * self.clock

    def exec(self, cmd):
        match cmd.split():
            case ["noop"]:
                self.clock += 1
                self.add_signal()
            case ["addx", V]:
                self.clock += 1
                self.add_signal()
                self.clock += 1
                self.X += int(V)
                self.add_signal()

with open("input.txt") as f:
    cpu = CPU(20, 220, 40)
    for cmd in f.readlines():
        cpu.exec(cmd.strip())

print(cpu.sigsum)

    


