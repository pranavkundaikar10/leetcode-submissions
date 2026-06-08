class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+ 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        output = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                if len(output) == k:
                    break
                output.append(j)
        return output
