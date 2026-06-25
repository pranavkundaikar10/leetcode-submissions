class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl, pac = set(), set()

        def backtrack(i, j, ocean, prev):
            if min(i, j) < 0 or i >= rows or j >= cols or heights[i][j] < prev or (i, j) in ocean:
                return
            
            ocean.add((i, j))
            backtrack(i-1, j, ocean, heights[i][j])
            backtrack(i+1, j, ocean, heights[i][j])
            backtrack(i, j-1, ocean, heights[i][j])
            backtrack(i, j+1, ocean, heights[i][j])                                    



        for i in range(rows):
            backtrack(i, 0, pac, heights[i][0])
            backtrack(i, cols-1, atl, heights[i][cols-1])

        for j in range(cols):
            backtrack(0, j, pac, heights[0][j])
            backtrack(rows-1, j, atl, heights[rows-1][j])

        res = []

        for i in range(rows):
            for j in range(cols):
                if (i,j) in atl and (i,j) in pac:
                    res.append((i,j))
        return res
