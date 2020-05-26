# Implementation of a Hash Table #

class HashTable(object):
    
    def __init__(self,size):
        
        # Set up size and slots and data
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        # we will use integer keys for ease of use with the Hash Function #
        
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        
        else:
            
            # If key already exists, replace old value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  
            
            # Otherwise, find the next available position #
            else:
                
                nextslot = self.rehash(hashvalue,len(self.slots))
                
                # Get to the next slot
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                # Set new key, if NONE
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                    
                # Otherwise replace old value
                else:
                    self.data[nextslot] = data 

    def hashfunction(self,key,size):
        # Remainder Method #
        return key%size

    def rehash(self,oldhash,size):
        # For finding next possible positions #
        return (oldhash+1)%size
    
    
    def get(self,key):
        
  
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        
        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

hash_table = HashTable(6)
hash_table[1] = "one"
hash_table[2] = "two"
hash_table[3] = "three"
print(hash_table[1])

hash_table[1] = "new_value"

print(hash_table[1])

    
    
