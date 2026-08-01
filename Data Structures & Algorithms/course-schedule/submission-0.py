class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        state = [0] * numCourses

        for i, j in prerequisites:
            adj[j].append(i)
        print(f'{adj}')
        def dfs(i):
            if state[i] == 1:
                return False
            if state[i] == 2:
                return True
            
            state[i] = 1
            for neighbor in adj[i]:
                if not dfs(neighbor):
                    return False
            state[i] = 2
            return True
        
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True
