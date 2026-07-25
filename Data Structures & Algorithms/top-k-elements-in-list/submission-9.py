class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums)+1)]
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1

        for key, val in mp.items():
            count[val].append(key)
        
        res = []
        for i in range(len(count)-1, -1, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res


