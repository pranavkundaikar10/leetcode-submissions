class UnionFind:

    def __init__(self, n):
        self.parents= {i: i for i in range(1, n+1)}
        self.ranks = {i: 1 for i in range(1, n+1)}
        self.count = n

    def find(self, p):
        if self.parents[p] != p:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        res = []
        for u, v in edges:
            if not uf.union(u, v):
                res.append([u, v])
        print(res)
        print(uf.parents)
        return res[-1]



        
