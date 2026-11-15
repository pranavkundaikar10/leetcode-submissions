class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False, l, r
                l += 1
                r -= 1
                
            return True, l, r

        status, l, r = isPalindrome(0, len(s)-1)
        if not status:
            return isPalindrome(l+1, r)[0] or isPalindrome(l, r-1)[0]

        return True
                
