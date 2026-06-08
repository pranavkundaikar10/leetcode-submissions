class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board:
            return False

        def dfs(i, j, foundIdx, seen):
            if foundIdx == len(word):
                print("final", seen)
                return True
            # print(i, j)
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i,j) in seen:
                return False
            if board[i][j] != word[foundIdx]:
                return False
            print("found", i, j, foundIdx, word[foundIdx])                
            foundIdx += 1
            seen.add((i, j))
            status = (dfs(i+1, j, foundIdx, seen) or dfs(i-1, j, foundIdx, seen) or dfs(i,j-1, foundIdx, seen) or dfs(i,j+1, foundIdx, seen))
            seen.remove((i,j))
            return status
            

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        return False

        