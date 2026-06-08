class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        ss = set() # set of elements

        l = 0
        r = 0
        while r < len(s):
            print(s[r])
            if s[r] in ss:
                print("in if", l, r, max_len, ss)
                ss.remove(s[l])
                l += 1
                print(l, r, max_len, ss)
            else:
                print("in else", l, r, max_len, ss)
                ss.add(s[r])
                r += 1
                max_len = max(r-l, max_len)
                print(l, r, max_len, ss)                
            print("\n---")


        return max_len


        