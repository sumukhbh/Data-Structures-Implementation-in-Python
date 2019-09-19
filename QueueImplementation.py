class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Enqueue(self,item):
        return (self.items.insert(0,item))

    def Dequeue(self):
        return (self.items.pop())

    def size(self):
        return len(self.items)

Q = Queue()
print(Q.isEmpty())
Q.Enqueue(3)
Q.Enqueue(6)
Q.Enqueue("False")
Q.Dequeue()
print(Q.size())
