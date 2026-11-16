class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        def dfs(i, subset):
            print(subset)
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                print(s[i:j+1])
                if not isPalindrome(s[i:j+1]):
                    continue
                subset.append(s[i:j+1])
                dfs(j+1, subset)
                subset.pop()

        dfs(0, [])
        return res



        