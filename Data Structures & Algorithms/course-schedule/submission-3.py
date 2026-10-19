class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adj = {i:[] for i in range(numCourses)}
        indegree = defaultdict(int)        
        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)


        visited = set()

        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)

            for n in adj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        return len(visited) == numCourses

