class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {}

        for i in range(0, len(nums)):
            if nums[i] not in numCounts:
                numCounts[nums[i]] = 1
            else:
                numCounts[nums[i]] += 1
        sortedCounts = dict(sorted(numCounts.items(), key=lambda item: item[1], reverse=True))

        result = []
        count = 0

        for key in sortedCounts:
            count += 1
            if count <= k:
                result.append(key)
        return result
        