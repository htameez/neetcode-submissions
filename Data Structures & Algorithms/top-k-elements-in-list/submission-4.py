class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {}

        for i in range(len(nums)):
            if nums[i] not in numCounts:
                numCounts[nums[i]] = 1
            else:
                numCounts[nums[i]] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in numCounts.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        