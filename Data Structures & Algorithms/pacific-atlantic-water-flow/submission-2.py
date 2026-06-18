class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()
        def dfs(i, j, subset, prev, visited):
            if i < 0 or j < 0 or i >= rows or j >= cols or heights[i][j] < prev or (i, j) in visited:
                return

            if subset == 'atl':
                atl.add((i, j))
            if subset == 'pac':
                pac.add((i, j))
            visited.add((i, j))
            dfs(i-1, j, subset, heights[i][j], visited)
            dfs(i+1, j, subset, heights[i][j], visited)
            dfs(i, j+1, subset, heights[i][j], visited)
            dfs(i, j-1, subset, heights[i][j], visited)

        for r in range(rows):
            dfs(r, 0, 'pac', float('-inf'), set())
            dfs(r, cols-1, 'atl', float('-inf'), set())

        for c in range(cols):
            dfs(0, c, 'pac', float('-inf'), set())
            dfs(rows-1, c, 'atl', float('-inf'), set())


        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r,c)in pac:
                    res.append([r, c])
        return res