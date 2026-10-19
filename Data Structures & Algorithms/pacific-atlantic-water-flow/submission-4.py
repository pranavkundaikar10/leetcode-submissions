class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        rows, cols = len(heights), len(heights[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c, flag):
            nonlocal atl, pac
            if flag == "atl":
                sea = atl
            else:
                sea = pac
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in sea:
                return
            sea.add((r,c))

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if min(nr,nc) < 0 or nr >= rows or nc >= cols or heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, flag)

        for r in range(rows):
            dfs(r, 0, "pac")
            dfs(r, cols-1, "atl")

        for c in range(cols):
            dfs(0, c, "pac")
            dfs(rows-1, c, "atl")

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r, c])
        return res


            






        
