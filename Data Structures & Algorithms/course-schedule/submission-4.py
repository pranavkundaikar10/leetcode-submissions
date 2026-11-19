class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, dependency in prerequisites:
            adj[dependency].append(course)
            indegrees[course] += 1

        queue = deque()
        for course, dependency in enumerate(indegrees):
            if dependency == 0:
                queue.append(course)

        visited = set()
        while queue:
            course = queue.popleft()

            visited.add(course)

            for dependency in adj[course]:
                if dependency in visited:
                    continue
                indegrees[dependency] -= 1
                if indegrees[dependency] == 0:
                    queue.append(dependency)
        
        return True if len(visited) == numCourses else False

                






        
