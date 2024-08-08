class CPU:
    def __init__(self, ram, es) -> None:
        self.ram = ram
        self.es = es
        self.PC = 0
    
    def run(self, addr):
        self.PC = addr
        a = self.ram.read(self.PC)
        b = self.ram.read(self.PC + 1)
        c = 1
        while a <= b:
            self.ram.write(a, c)
            self.es.output(f"{a} <- {c}\n")
            c += 1
            a += 1

class RAM:
    def __init__(self, k) -> None:
        self.mem = []
        for i in range(2**k):
            self.mem.append(0)
    
    def read(self, addr):
        return self.mem[addr]
    
    def write(self, addr, data):
        self.mem[addr] = data
    
    def capacity(self):
        return len(self.mem)
    
class IO:
    def __init__(self) -> None:
        print('IO Created')
    
    def output(self, msg):
        print(msg, end='')
    
    def input(self, prompt):
        return input(prompt)

def main():
    es = IO()
    ram = RAM(7)
    cpu = CPU(ram, es)
    
    #es.output(ram.capacity() + '\n')
    
    ram.write(0, 10)
    ram.write(1, 20)
    cpu.run(0)

if __name__ == '__main__':
    main()