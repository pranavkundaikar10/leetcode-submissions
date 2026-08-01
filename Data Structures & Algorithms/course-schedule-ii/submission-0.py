class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(len(indegree)) if indegree[i]==0])
        res = []
        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if processed == numCourses else []
