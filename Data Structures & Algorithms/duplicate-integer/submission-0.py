class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        for k, count in counter.items():
            if count > 1:
                return True
        return False  