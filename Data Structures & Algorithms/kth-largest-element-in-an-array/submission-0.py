class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            heapq.heappush(arr, num)
            while len(arr) > k:
                heapq.heappop(arr)
        return arr[0] if arr else 0
        