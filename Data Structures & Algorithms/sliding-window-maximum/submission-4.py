class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        arr = []
        while r < len(nums):
            # print(r, nums[r], arr, res)
            heapq.heappush(arr, (-nums[r], r))
            print('arr push', arr)
            print(r-l+1, arr[0][1], 'l', l)
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                while arr[0][1] < l:
                    val = heapq.heappop(arr)
                    print('popping', val)
                res.append(-arr[0][0])
            r += 1
        return res
        