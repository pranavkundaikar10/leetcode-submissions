# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs)//2

        left, right = self.mergeSort(pairs[:mid]), self.mergeSort(pairs[mid:])
        return self.merge(left, right)

    def merge(self, a, b):
        res = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i].key <= b[j].key:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        if i < len(a):
            res.extend(a[i:])
        if j < len(b):
            res.extend(b[j:])
        return res




