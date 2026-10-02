class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r-l)//2

            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(pile/mid)

            if totaltime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
    
        return res