class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        max_ele = -1
        for i in range(n-1, -1, -1):
            res[i]  = max_ele
            max_ele = max(arr[i], max_ele)
        return res