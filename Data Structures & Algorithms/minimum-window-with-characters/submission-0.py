
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count c in t
        # init have and need
        resLen = float('infinity')
        res = [0, 0]
        c_t, window = {}, {}
        
        l, r = 0, 0
        for c in t:
            c_t[c] = c_t.get(c, 0) + 1
        have, need = 0, len(c_t)
        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in c_t and window[c] == c_t[c]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in c_t and window[s[l]] < c_t[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r+1] if resLen!= float('infinity') else ''
            
        