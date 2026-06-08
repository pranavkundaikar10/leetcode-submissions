# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        for pair in pairs:
            print(pair.key)
        if len(pairs) <= 1:
            return pairs
        m = len(pairs)//2
        print('mid point', m)
        b = self.mergeSort(pairs[:m])
        c = self.mergeSort(pairs[m:])
        return self.merge(b, c)
    
    def merge(self, l1, l2):
        l3 = []
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i].key <= l2[j].key:
                l3.append(l1[i])
                i += 1
            else:
                l3.append(l2[j])
                j += 1
        while i < len(l1):
            l3.append(l1[i])
            i+=1
        while j < len(l2):
            l3.append(l2[j])
            j+=1
        return l3

