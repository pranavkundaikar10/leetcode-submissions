class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return False

        if self.rank[pi] < self.rank[pj]:
            self.parent[pi] = pj
        elif self.rank[pj] < self.rank[pi]:
            self.parent[pj] = pi
        else:
            self.parent[pj] = pi
            self.rank[pi] += 1
        
        self.count -= 1
        return True



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        dsu = DSU(n)
        for i, j in edges:
            if not dsu.union(i, j):
                return False
        return True
        