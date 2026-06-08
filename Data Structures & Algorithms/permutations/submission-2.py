class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for i in range(len(nums)):
            newPerms = []
            for perm in perms:
                for j in range(len(perm)+1):
                    pCopy = perm.copy()
                    pCopy.insert(j, nums[i])
                    newPerms.append(pCopy)
            perms = newPerms
        return perms