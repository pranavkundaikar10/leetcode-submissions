class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        res = []
        def dfs(root):
            while adj[root]:
                dfs(heapq.heappop(adj[root]))
            res.append(root)
            return
        dfs("JFK")
        return res[::-1]