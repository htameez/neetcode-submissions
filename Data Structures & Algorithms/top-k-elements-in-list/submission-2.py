class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {}

        for i in range(len(nums)):
            if nums[i] not in numCounts:
                numCounts[nums[i]] = 1
            else:
                numCounts[nums[i]] += 1
        sortedCounts = sorted(numCounts.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sortedCounts[i][0])
        return result
        