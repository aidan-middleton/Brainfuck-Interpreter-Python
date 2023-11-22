import sys

class BrainFuck:
    def __init__(self):
        self.memory = [0]
        self.pointer = 0
        
        self.program = ''
        self.program_counter = 0

    def reinitialize(self):
        self.memory = [0]
        self.pointer = 0
        
        self.program = ''
        self.program_counter = 0
    
    def read(self, program):
        temp = []
        for char in program:
            if char in ['>', '<', '+', '-', '[', ']', ',', '.']:
                temp.append(char)
        program = temp
        stack = []
        for i in range(len(program)):
            char = program[i]
            if char == '[':
                stack.append(i)
            if char == ']':
                if not stack:
                    print('ERROR: Unmatched brackets')
                    sys.exit(1)
                head = stack.pop()
                program[head] = i
                program[i] = -head
        if stack:
            print('ERROR: Unmatched brackets')
            sys.exit(1)
        self.program = program
        
    def execute(self):
        command = self.program[self.program_counter]
        
        while self.program_counter < len(self.program):
            command = self.program[self.program_counter]
            if command == '>':
                if self.pointer == len(self.memory) - 1:
                    self.memory.append(0) 
                self.pointer += 1
            elif command ==  '<':
                if self.pointer == 0:
                    print('ERROR: Pointer out of range')
                    sys.exit(1)
                self.pointer -= 1
            elif command ==  '+':
                self.memory[self.pointer] += 1
            elif command ==  '-':
                self.memory[self.pointer] -= 1
            elif command == ',':
                input = input()
                self.memory[self.pointer] = ord(input[0])
            elif command == '.':
                print(chr(self.memory[self.pointer]), end='')
            else:
                if command < 0:
                    self.program_counter = -command
                    continue
                else:
                    if self.memory[self.pointer] == 0:
                        self.program_counter = command
            self.program_counter += 1
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python BrainFuck.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        program = []
        for line in file:
            for char in list(line):
                program.append(char)
        bf = BrainFuck()
        bf.read(program)
        bf.execute()
