class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums)+ 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for item, count in counter.items():
            freq[count].append(item)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                if len(res) == k:
                    break
                res.append(num)
        return res
                