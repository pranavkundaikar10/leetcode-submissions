class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        bucket = [[] for i in range(len(nums)+1)]
        for key, value in mp.items():
            bucket[value].append(key)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
            