class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        n = len(s)
        max_res = 0
        for r in range(n):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_res = max(max_res, r-l+1)
            r += 1
        return max_res