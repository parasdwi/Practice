class Solution(object):
    def largestPerimeter(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=len(nums)-1
        nums.sort()
        if len(nums)<3:
            return 0
        while (i>=2):
            if nums[i-2]+nums[i-1]>nums[i]:
                return nums[i-2]+nums[i-1]+nums[i]
            i-=1
        return 0


            