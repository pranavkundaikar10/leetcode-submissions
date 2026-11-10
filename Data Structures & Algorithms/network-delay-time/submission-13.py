class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((t, v))

        heap = [(0, k)]
        visited = set()

        while heap:
            curr_time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return curr_time
            for time, neigh in adj[node]:
                if neigh in visited:
                    continue
                heapq.heappush(heap, (curr_time+time, neigh))

        return -1

