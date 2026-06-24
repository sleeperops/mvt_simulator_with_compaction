class Memory:  # size = size of memory, fill = initial value of each memory block, array = the actual writable memory array
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
    
    # loads the contents of the process into memory
    def load(self, process):
        print("load in progress...")
        for i in range(process.size):
            print(f"Current block: memory[{i}] = {self.array[i+process.start]}")
            self.array[i + process.start] += 1
            print(f"    -> memory[{i}] = {self.array[i+process.start]}")
            
    def deallocate(self, process):
        print("deallocate in progress...")
        for i in range(process.size):
            print(f"Current block: memory[{i + process.start}] = {self.array[i+process.start]}")
            self.array[i + process.start] -= 1
            print(f"    -> memory[{i}] = {self.array[i+process.start]}")

    # Checks for an available spot in the memory and fills it up 
    def allocate(self, process):  #!put the start parameter here 
        target_end= process.start + process.size
        if target_end > self.size:  #Either process is too big or external fragmentation
            print("cannot be")  # process too big
            return 1
        
        else:  # check if target section is free
            for address, block in enumerate(self.array[process.start:]):  # address is the index and block is the value inside that index
                if block != 0:
                    print(f"{self}[{address}] = {block}  // OCCUPIED !") #!add return
                    return 1
            else:
                print("Can allocate blocks")
                print("Memory section is available") #!add return
                self.load(process)
                return 0
                
    
class Process:
    def __init__(self, name, size, start = 0):
        self.name = name
        self.size = size
        self.start = start  # what part of the memory the process willbe inserted

# For testing purposes
class Details: 
    
    def display_memory(memory):
        for address, block in enumerate(memory.array):
            print(f"memory[{address}] = {block}")
    
    def display_remaining(memory):
        count = 0
        for i in memory.array:
            if i == 0:
                count +=1
        return count
        
memory_1 = Memory(32, 0) # 0-31, !Make 32 a variable
p1 = Process("A",16 , 0)
p2 = Process("B", 10, 10)

memory_1.array[4] = 0

memory_1.allocate(p1)

Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")

memory_1.deallocate(p1)
Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")
print("Done")