class Memory:  # size = size of memory, fill = initial value of each memory block, array = the actual writable memory array
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
    
    
    def transfer(self, process):
        print("Transfer in progress...")
        for i in range(process.size):
            print(f"Current block: memory[{i}] = {self.array[i+process.start]}")
            self.array[i + process.start] += 1
            print(f"    -> memory[{i}] = {self.array[i+process.start]}")

        # checks if memory section is available 
    def load(self, process):  #!put the start parameter here 
        target_end= process.start + process.size
        if target_end > self.size:  #Either process is too big or external fragmentation
            print("cannot be")  # process too big
        
        else:  # check if target section is free
            for address, block in enumerate(self.array[process.start:]):  # address is the index and block is the value inside that index
                if block == 0:
                    print(f"{self}[{address}] = {block}  // OK") # ! add return
                    
                elif block != 0:
                    print(f"{self}[{address}] = {block}  // OCCUPIED !") #!add return
                    break
            else:
                print("Can load blocks")
                print("Memory section is available") #!add return
                
                # transfer
                self.transfer(process)
    
class Process:
    def __init__(self, name, size, start = 0):
        self.name = name
        self.size = size
        self.start = start

class Details:
    
    def display_memory(memory):
        for address, block in enumerate(memory.array):
            print(f"memory[{address}] = {block}")
    
    def display_remaining(memory):
        count = 0
        for i in memory.array:
            if memory.array[i] == 0:
                count +=1
        return count
        
memory_1 = Memory(32, 0) # 0-31, !Make 32 a variable
p1 = Process("A", 4, 1)
p2 = Process("B", 10, 10)
p2 = Process("C", 20, 12)

memory_1.array[4] = 0

memory_1.load(p1)
memory_1.load(p2)
print(memory_1.array[0])
print(memory_1.array[4])

print(Details.display_memory(memory_1))
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")