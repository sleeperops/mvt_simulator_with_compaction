class Memory:  # size = size of memory, fill = initial value of each memory block, array = the actual writable memory array
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
    
    def compact(self):
        compacted_result = []
        
        for address in range(self.size):  # creates a new array and append all of the non zero values from the previous array contigiously
            if self.array[address] != 0:
                compacted_result.append(self.array[address])  
        print("New temp array created")
        size_difference = self.size - len(compacted_result)  # take the size diff of two arrays and complete the new array with it
        compacted_result.extend([0]*size_difference)  # complete the new array
        self.array = compacted_result
        print("Array compacted")
    
    # loads the contents of the process into memory
    def load(self, process, process_start):
        print("LOADING PROCESS...")
        for i in range(process.size):
            print(f"Current block: memory[{i + process_start}] = {self.array[i+process_start]}")
            self.array[i + process_start] = process.name
            print(f"    -> memory[{i + process_start}] = {self.array[i+process_start]}")
            
    def deallocate(self, process, process_start):
        print(f"DEALLOCATING PROCESS: {process.name}")
        for i in range(process.size):
            print(f"Current block: memory[{i + process_start}] = {self.array[i+process_start]}")
            self.array[i + process_start] = 0
            print(f"    -> memory[{i + process_start}] = {self.array[i+process_start]}")

    # allocate a section of memory for a specific process
    def allocate(self, process, process_start):  #!put the start parameter here
        print(f"ALLOCATING PROCESS: {process.name}")
        target_end= process_start + process.size
        if target_end > self.size:  #Either process is too big or external fragmentation
            print("cannot be")  # process too big
            return 1
        
        else:  # check if target section is free
            for address in range(process_start,target_end):  # address is the index and block is the value inside that index
                if self.array[address] != 0:
                    print(f"{self}[{address}] = {self.array[address]}  // OCCUPIED !") #!add return
                    return 1
            else:
                print("Can allocate blocks")
                print("Memory section is available") #!add return
                self.load(process, process_start)
                self.compact()
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
p1 = Process("A",4)
p2 = Process("B", 10)
p3 = Process("C", 10)

memory_1.array[4] = 0

memory_1.allocate(p1,0)
memory_1.allocate(p2,5)
memory_1.allocate(p3,16)

Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")

print("DEALLOCATING P1")
memory_1.deallocate(p1, 0)
Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")

print("DEALLOCATING P2")
memory_1.deallocate(p2,5)
Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")

print("DEALLOCATING P3")
memory_1.deallocate(p3,16)
Details.display_memory(memory_1)
print(f"Remaining memory slots:{Details.display_remaining(memory_1)} ")



print("Done")

