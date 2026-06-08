class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = heights
        rows, cols = len(heights), len(heights[0])
        res = []

        def bfs(i, j):
            check = False
            # if (i, j) == (0,2): check = True
            if i == 0 and j == 0: check = True
            if check: print('starting', i, j)            
            q = collections.deque()
            q.append((i,j))
            val = h[i][j]
            atl, pac = False, False
            seen = set((i, j))
            while q and (not atl or not pac):
                for k in range(len(q)):
                    loc = q.popleft()
                    if check: print('loc', loc)
                    neighbors = [(-1, 0),(0, -1), (1, 0), (0, 1)]
                    for neighbor in neighbors:
                        if loc[0]+ neighbor[0] < 0 or loc[1]+neighbor[1] < 0:
                            if check: print("pacific found", loc[0]+ neighbor[0], loc[1]+neighbor[1])
                            pac = True
                            continue
                        if loc[0]+ neighbor[0] == rows or loc[1]+neighbor[1] == cols:
                            if check: print("atlantic found",loc[0]+ neighbor[0], loc[1]+neighbor[1])
                            atl = True
                            continue
                        if h[loc[0]][loc[1]] < h[loc[0]+ neighbor[0]][loc[1]+ neighbor[1]] or (loc[0]+ neighbor[0], loc[1]+ neighbor[1]) in seen:
                            if check: print("skipping", loc[0]+ neighbor[0], loc[1]+neighbor[1])
                            continue
                        q.append((loc[0]+ neighbor[0], loc[1]+ neighbor[1]))
                        seen.add((loc[0]+ neighbor[0], loc[1]+ neighbor[1]))
            if check: print("finished", atl, pac)
            if atl and pac:
                print("found both", i, j)
                return True
            return False

        res = []
        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append([i,j])
        return res
        