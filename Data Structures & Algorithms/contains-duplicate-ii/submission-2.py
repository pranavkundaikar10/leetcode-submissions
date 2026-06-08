class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r, seen = 0, 0, set()
        while r < len(nums):
            while r - l > k:
                seen.remove(nums[l])
                l += 1
            if r != l and nums[r] in seen:
                return True
            seen.add(nums[r])                
            r += 1
        return False
        