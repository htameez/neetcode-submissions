class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # for each element in the array
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
        # loop thru all other elements and fidn product
                if i != j:
                    product *= nums[j]

        # add to new array with product at current element's index
            result.append(product)

        return result

        