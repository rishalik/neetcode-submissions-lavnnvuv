class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.check_count(s) == self.check_count(t)
    
    def check_count(self, s):
        count = {}
        for i in s:
            if i not in count:
                count[i] =0
            count[i] += 1
        return count