class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.count = n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return False
        
        if self.ranks[pi] < self.ranks[pj]:
            self.parents[pi] = pj
        elif self.ranks[pj] < self.ranks[pi]:
            self.parents[pj] = pi
        else:
            self.parents[pj] = pi
            self.ranks[pi] += 1
        self.count -= 1
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i, j)
        return uf.count
                


