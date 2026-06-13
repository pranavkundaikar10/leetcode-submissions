# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i, pair in enumerate(pairs):
            for j in range(i-1, -1, -1):
                if pairs[j].key <= pairs[j+1].key:
                    break
                else:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
            res.append(list(pairs))
        return res

        