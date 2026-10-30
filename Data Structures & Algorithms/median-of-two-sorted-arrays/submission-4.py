class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # swap to makes nums1 smaller
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        # add 1 to ensure that right side always chooses more elements
        half = (m + n + 1) // 2

        # run binary search on smaller
        # partition cut answer space.

        # since its partition based, we initialise to m 
        # and we could end up at 0 as well.
        # so we use floats to handle outer boundaries
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            max_left_a = nums1[i-1] if i > 0 else float("-inf")
            min_right_a = nums1[i] if i < m else float("inf")
            max_left_b = nums2[j-1] if j > 0 else float("-inf")
            min_right_b = nums2[j] if j < n else float("inf")

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m+n) % 2 == 1:
                    return float(max(max_left_a, max_left_b))
                return float((max(max_left_a, max_left_b) + min(min_right_a, min_right_b))/2.0)
            elif max_left_a > min_right_b:
                r = i - 1
            else:
                l = i + 1





        