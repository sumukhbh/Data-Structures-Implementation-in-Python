# Union Find Data Structure #

class UnionFind(object):
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, val):
        return self.root[val]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)

def main():
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # True
    print(uf.connected(5, 7))  # True
    print(uf.connected(4, 9))  # False




