class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_bracket = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in dict_bracket:
                stack.append(dict_bracket[i])
            else:
                if not stack:
                    return False
                if stack.pop() != i:
                    return False
        if stack:
            return False
        return True