class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board:
            return False
        seen = set()
        def dfs(i, j, foundIdx):
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
            status = (dfs(i+1, j, foundIdx) or dfs(i-1, j, foundIdx) or dfs(i,j-1, foundIdx) or dfs(i,j+1, foundIdx))
            seen.remove((i,j))
            return status
            

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

        