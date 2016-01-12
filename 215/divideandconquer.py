class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print nums, k
        midIndex = (len(nums) / 2) - 1
        mid = nums[midIndex]
        smaller = []
        bigger = []
        equal = []
        for x in nums:
            if x < mid:
                smaller.append(x)
            elif x > mid:
                bigger.append(x)
            else:
                equal.append(x)
        
        print smaller, equal, bigger
        
        if len(bigger) == k - 1:
            return mid
        elif len(bigger) >= k:
            return self.findKthLargest(bigger, k)
        else: # len(bigger) < k - 1
            if len(smaller) >= k - len(equal) - len(bigger) \
            and k - len(equal) - len(bigger) > 0:
                return self.findKthLargest(smaller, k - len(equal) - len(bigger))
            else:
                return mid
