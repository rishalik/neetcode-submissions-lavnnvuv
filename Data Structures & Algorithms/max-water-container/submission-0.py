class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        best = 0
        while l < r:
            height = r - l
            width = heights[l] if heights[l] < heights[r] else heights[r] 
            area = height * width
            if area > best:
                 best = area 
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best


