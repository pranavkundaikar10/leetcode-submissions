class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        if len(arr) < k:
            return res
        l, r = 0, 0
        sum = 0
        while r < len(arr):
            if r - l + 1 > k:
                sum -= arr[l]
                l += 1
                continue
            sum += arr[r]
            if r - l + 1 == k and sum/k >= threshold:
                res += 1
            r += 1
        return res
        