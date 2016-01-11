class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere = maxSoFar = nums[0]
        for x in nums[1:]:
            maxEndingHere = max(x, maxEndingHere + x)
            maxSoFar = max(maxSoFar, maxEndingHere)
        
        return maxSoFar
