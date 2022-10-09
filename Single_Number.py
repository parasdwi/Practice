# FASTER THAN 92.5% SUBMISSIONS

class Solution(object):
    def singleNumber(self, nums):
        i,j=0,1
        nums.sort()
        while(j<len(nums)):
            if nums[i]==nums[j]:
                i+=2
                j+=2
            else:
                return nums[i]
        return nums[len(nums)-1]
