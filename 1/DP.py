class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in table:
                return [table[diff] + 1, i + 1]
            else:
                table[nums[i]] = i

        return [-1, -1]
