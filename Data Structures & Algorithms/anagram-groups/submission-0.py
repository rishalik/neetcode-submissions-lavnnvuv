from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for i in s:
                counts[ord(i) - ord('a')] += 1
            counter[tuple(counts)].append(s)
        return sorted(counter.values(), key=len)
