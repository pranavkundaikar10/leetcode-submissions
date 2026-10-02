# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs))

    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs
        
        m = (s+e) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m+1, e)
        self.merge(pairs, s, m, e)
        return pairs

    def merge(self, pairs, s, m, e):
        l = pairs[s:m+1]
        r = pairs[m+1: e+1]
        i, j, k = 0, 0, s
        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                pairs[k] = l[i]
                i += 1
            else:
                pairs[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            pairs[k] = l[i]
            k += 1
            i += 1
        
        while j < len(r):
            pairs[k] = r[j]
            k += 1
            j += 1
        

