class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        table = {}
        m = 0
        for i in range(0, len(s)):
            if (s[i] in table) and (table[s[i]] >= m):
                m = table[s[i]] + 1
            else:
                maxLength = max(maxLength, i - m + 1)
            table[s[i]] = i
        return maxLength
