class Memory:
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
class Process:
    def __init__(self, name, size, start):
        self.name = name
        self.size = size
        self.start = start
    

        
        
memory_1 = Memory(32, 0) # !Make 32 a variable
print(memory_1.array[23])

