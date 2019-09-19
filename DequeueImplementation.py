class Dequeue(object):
    def __init__(self):
        self.items = []   
    def isEmpty(self):
        return self.items == []
    def insert_front(self, item):
        return self.items.append(item)
    def insert_rear(self, item):
        return self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

d = Dequeue()
d.insert_front("abc")
d.insert_rear(2)
print(d.size())
d.remove_front()
print(d.size())

