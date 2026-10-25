class UnionFind:


    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
        self.components = n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        
        if self.ranks[pi] < self.ranks[pj]:
            self.parents[pi] = pj
        elif self.ranks[pi] > self.ranks[pj]:
            self.parents[pj] = pi
        else:
            self.parents[pj] = pi
            self.ranks[pi] += 1
        
        self.components -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.components
