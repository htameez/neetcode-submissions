class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort array
        nums.sort()
        numbers = {}
        # make hash table with key as index and value as num in nums
        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            numbers[nums[i]] = i
        return False
        