class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
            
        opt = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i == 1:
                        opt[i] = 2
                    else:
                        opt[i] = opt[i-2] + 2
                elif (i - opt[i-1] - 1 >= 0) and s[i - opt[i-1] - 1] == '(':
                    opt[i] = opt[i-1] + 2 + opt[i - opt[i-1] - 2]
        
        return max(opt)
