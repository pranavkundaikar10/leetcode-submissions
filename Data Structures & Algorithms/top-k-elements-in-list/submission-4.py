class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in counts.items():
            buckets[val].append(key)
        
        i = 0
        output = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                if len(output) == k:
                    break
                output.append(num)                    
        return output

        