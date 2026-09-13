class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxArea = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        # find prefix and suffix maximum for each index
        prefix[0] = height[0]
        for i in range(len(height)):
            prefix[i] = max(prefix[i - 1], height[i])
        
        suffix[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])
        
        # compute max area using prefix and suffix maximums and current height
        for i in range(len(height)):
            maxArea += min(prefix[i], suffix[i]) - height[i]

        return maxArea
