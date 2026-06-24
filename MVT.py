class Memory:  # size = size of memory, fill = initial value of each memory block, array = the actual writable memory array
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
class Process:
    def __init__(self, name, size, start = None):
        self.name = name
        self.size = size
        self.start = start
    
    def load(memory, process):
        blocks_to_occupy= process.start + process.size
        if blocks_to_occupy > memory.size:  #Either process is too big or external fragmentation
            return "cannot be"  # process too big
        else:  # check if the blocks to be occupied are free
            for block in memory.array:
                if memory.array[block] == 0:
                    print("OK")
                elif memory.array[block] == 1:
                    print("Occupied")
                    break
                else:
                    print("Occupied with unknown value")
                    break
            else:
                print("Can load blocks")
                return "Memory section is available"
                
                
        
memory_1 = Memory(32, 0) # !Make 32 a variable
p1 = Process("A", 16, 0)

print(Process.load(memory_1, p1))
print(memory_1.array[0])


