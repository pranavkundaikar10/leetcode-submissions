class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        
        cnt = [[] for _ in range(len(nums)+1)]
        for key, val in hmap.items():
            cnt[val].append(key)

        res = []
        for i in range(len(cnt)-1, -1, -1):
            for val in cnt[i]:
                if len(res) == k:
                    break
                res.append(val)


        return res