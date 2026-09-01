from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            counter[tuple(count)].append(s)
        return sorted(counter.values(), key=len)
