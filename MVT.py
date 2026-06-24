class Memory:  # size = size of memory, fill = initial value of each memory block, array = the actual writable memory array
    def __init__(self,size, fill):
        self.size = size
        self.fill = fill
        self.array = [fill] * size
        self.free_space = self.display_remaining()
        
    def display_memory(memory):
        for address, block in enumerate(memory.array):
            print(f"memory[{address}] = {block}")
    
    def display_remaining(memory):
        count = 0
        for i in memory.array:
            if i == 0:
                count +=1
        return count
    
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
            
    def deallocate(self, process):
        print(f"DEALLOCATING PROCESS: {process.name}")
        new_process_start = (self.array).index(process.name)  # gets the new starting position of the process post compaction
        for i in range(process.size):
            print(f"Current block: memory[{i + new_process_start}] = {self.array[i + new_process_start]}")
            self.array[i + new_process_start] = 0
            print(f"    -> memory[{i + new_process_start}] = {self.array[i + new_process_start]}")
        
        self.compact()

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

