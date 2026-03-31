class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for n in nums_set:
            if (n-1) not in nums_set:
                length = 1
                while (length+n) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest

            