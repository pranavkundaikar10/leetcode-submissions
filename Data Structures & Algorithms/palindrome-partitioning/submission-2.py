class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, subset):
            if i == len(s):
                res.append(subset[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1, subset)
                    subset.pop()
        dfs(0, [])
        return res


    def isPalindrome(self, s):
        if not s:
            return False
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True