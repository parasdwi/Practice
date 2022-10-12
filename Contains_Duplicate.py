class Solution(object):
    def containsNearbyDuplicate(self ,nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(list(set(nums))) or nums==[] or k==0:
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j-i<=k and nums[i]==nums[j]:
                    return True
        return False
