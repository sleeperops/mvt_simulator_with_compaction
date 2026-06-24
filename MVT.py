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

# checks if memory section is available 
def load(memory, process):
    target_end= process.start + process.size
    if target_end > memory.size:  #Either process is too big or external fragmentation
        return "cannot be"  # process too big
    
    else:  # check if target section is free
        for address, block in enumerate(memory.array):  # address is the index and block is the value inside that index
            if block == 0:
                print(f"{memory}[{address}] = {block}  // OK")
                
            elif block != 0:
                print(f"{memory}[{address}] = {block}  // OCCUPIED !")
                break
        else:
            print("Can load blocks")
            print("Memory section is available")
            
            # transfer
def transfer(memory, process, target_start, target_end):
    for i in range(process.size):
        memory.array[i + target_start] += 1
        
    

                
        
memory_1 = Memory(32, 0) # 0-31, !Make 32 a variable
p1 = Process("A", 16, 0)

memory_1.array[4] = 1

print(load(memory_1, p1))
print(memory_1.array[0])
print(memory_1.array[4])

