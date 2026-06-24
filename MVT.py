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

def transfer(memory, process):
    print("Transfer in progress...")
    for i in range(process.size):
        print(f"Current block: memory[{i}] = {memory.array[i+process.start]}")
        memory.array[i + process.start] += 1
        print(f"    -> memory[{i}] = {memory.array[i+process.start]}")

# checks if memory section is available 
def load(memory, process):  #!put the start parameter here 
    target_end= process.start + process.size
    if target_end > memory.size:  #Either process is too big or external fragmentation
        return "cannot be"  # process too big
    
    else:  # check if target section is free
        for address, block in enumerate(memory.array):  # address is the index and block is the value inside that index
            if block == 0:
                print(f"{memory}[{address}] = {block}  // OK") # ! add return
                
            elif block != 0:
                print(f"{memory}[{address}] = {block}  // OCCUPIED !") #!add return
                break
        else:
            print("Can load blocks")
            print("Memory section is available") #!add return
            
            # transfer
            transfer(memory,process)

def display_memory(memory):
    for address, block in enumerate(memory.array):
        print(f"memory[{address}] = {block}")
        
memory_1 = Memory(32, 0) # 0-31, !Make 32 a variable
p1 = Process("A", 3, 30)

memory_1.array[4] = 0

print(load(memory_1, p1))
print(memory_1.array[0])
print(memory_1.array[4])

display_memory(memory_1)
