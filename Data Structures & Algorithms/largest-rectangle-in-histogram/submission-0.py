class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # loop thru heights
        # keep stack for heights smaller than current height ot pop off current height
        # calculate max area by keeping max variable
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height* (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
            
                