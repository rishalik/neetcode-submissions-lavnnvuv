class Solution:

    def encode(self, strs: List[str]) -> str:
        val = ""
        for i in strs:
            val += str(len(i)) + "#" + i
        return val

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            i = j+1+length
            res.append(word)
        return res