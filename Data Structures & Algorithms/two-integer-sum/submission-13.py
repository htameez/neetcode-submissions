class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # difference = target - nums[i]
        vals = {}
        for i in range(len(nums)):
            difference = target - nums[i] 
            print(difference)
            if nums[i] in vals:
                return [vals[nums[i]], i]
            else:
                vals[difference] = i
            
        return []