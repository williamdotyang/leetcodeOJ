class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return None
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:len(nums)/2]
        nums2 = nums[len(nums)/2:]
        max1 = self.maxSubArray(nums1)
        max2 = self.maxSubArray(nums2)
        max12 = self.maxCrossArray(nums1, nums2)
        return max(max1, max2, max12)
    
    def maxCrossArray(self, nums1, nums2):
        maxSum1 = sum1 = nums1[-1]
        for i in range(len(nums1)-2, -1, -1):
            sum1 += nums1[i]
            if sum1 > maxSum1:
                maxSum1 = sum1

        maxSum2 = sum2 = nums2[0]
        for j in range(1, len(nums2)):
            sum2 += nums2[j]
            if sum2 > maxSum2:
                maxSum2 = sum2
        return maxSum1 + maxSum2
