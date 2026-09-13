class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # loop thru nums
        best = 1

        for i in range(len(nums)):
            start = nums[i]
            length = 1
            cur = start

            while True:
                found_next = False
                for j in range(len(nums)):
                    if nums[j] == cur + 1:
                        cur += 1
                        length += 1
                        found_next = True
                        break # break to avoid counting duplicates in array
                if not found_next: # if we didn't find the consecutive number if the whole array
                    break # break out of whole while loop

            best = max(best, length)
        
        return best
                
        
        # create hash table, where each set is a disjoint set, 
        # make disjoint sets with two numbers in each, both of which are one apart
        # union on disjoint sets to find consequitive sequence