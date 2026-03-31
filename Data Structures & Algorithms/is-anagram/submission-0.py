class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.count(s) == self.count(t)
    
    def count(self, string: str) -> dict:
        counter = {}
        for i in string:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        return counter
