class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere = maxSoFar = nums[0]
        for x in nums[1:]:
            maxEndingHere += x
            if x > maxEndingHere:
                maxEndingHere = x
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere
        
        return maxSoFar
