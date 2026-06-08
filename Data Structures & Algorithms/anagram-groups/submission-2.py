class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for i in item:
                count[ord(i)-ord('a')] += 1
            freq[tuple(count)].append(item)
        
        return list(freq.values())             
        