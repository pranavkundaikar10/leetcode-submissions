class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = k - 1
        sum = 0
        output = 0
        for j in range(len(arr)):
            sum += arr[j]
            if j - i + 1 == k:
                avg = sum/k
                if avg >= threshold:
                    output += 1
                sum -= arr[i]
                i += 1
        return output