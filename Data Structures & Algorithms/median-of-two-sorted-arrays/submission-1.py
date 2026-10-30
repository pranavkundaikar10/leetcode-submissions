class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2 # +1 to force more values on the right
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i
            min_A = nums1[i] if i < m else float("inf")
            max_A = nums1[i-1] if i > 0 else float("-inf")

            min_B = nums2[j] if j < n else float("inf")
            max_B = nums2[j-1] if j > 0 else float("-inf")

            if max_B <= min_A and max_A <= min_B:
                if (m+n) % 2 == 1:
                    return float(max(max_A, max_B))
                return float((max(max_A, max_B)+ min(min_A, min_B))/2.0)
            elif max_A > min_B:
                r = i - 1
            else:
                l = i + 1
            




        