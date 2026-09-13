class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # place pointer at start and end
        # check at each element if they add up to target
        # if not
            # if it's greater than target, decrement end pointer
            #if it's less than target, increment start pointer
        # return indices + 1
        l = 0
        r = len(numbers) - 1

        while l < r:
            if not numbers[l] + numbers[r] == target:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                else:
                    l += 1
            else:
                return [l + 1, r + 1]