class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxAmt = 0

        while l < r:
            currAmt = (r - l) * min(heights[l], heights[r])
            if currAmt > maxAmt:
                maxAmt = currAmt
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
            elif currAmt < maxAmt:
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
            else:
                l += 1
                r -= 1
        return maxAmt 