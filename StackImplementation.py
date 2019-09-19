class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items(len(self.items) - 1)

    def size(self):
        return len(self.items)

S = Stack()
print(S.isEmpty())
S.push(4)
S.push("Sumukh")
S.push(True)
S.pop()
print(S.size())



        

    
