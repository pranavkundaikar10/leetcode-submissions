class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

            if len(counts) <= 2:
                continue
            
            new_count = defaultdict(int)

            for num, count in counts.items():
                if count > 1:
                    new_count[num] = count - 1
                    
            counts = new_count
        res = []
        for key in counts:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res