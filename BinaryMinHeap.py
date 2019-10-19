# Binary MinHeap Implementation #

class BinHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    def heap_up(self,k):
        while k//2 > 0:                                   # Loop until it's not a root node  #
            if self.heap_list[k] < self.heap_list[k//2]:  # Check if the key value of child node is less than it's parent #
                temp_val = self.heap_list[k//2]           # Swap the parent and child if the above condition is true #
                self.heap_list[k//2] = self.heap_list[k]
                self.heap_list[k] = temp_val
            k = k//2
    def insert_heap(self,k):      
        self.heap_list.append(k)                 # Insert into list and increment size variable #
        self.curr_size += 1
        self.heap_up(self.curr_size)

    def find_min(self):
        return self.heap_list[1]

    def heap_down(self,k):                      # After the deletion of root, make swaps to push the new root to correct position #
        while k * 2 <= self.curr_size:
            min_val = self.min_node(k)
            if self.heap_list[k] > self.heap_list[min_val]:
                temp_val = self.heap_list[k]
                self.heap_list[k] = self.heap_list[min_val]
                self.heap_list[min_val] = temp_val
            k = min_val

    def min_node(self,k):
        if k*2+1 > self.curr_size:     
            return k*2
        else:
            if self.heap_list[k*2] < self.heap_list[k*2+1]: # Compare which child has the smaller key and return it's value #
                return k*2
            else:
                return k*2+1

    def delete_min(self):                        # Access the root element and remove it from the list #
        root_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        self.heap_list.pop()
        self.heap_down(1)
        return root_val
    
        




               
            
        

