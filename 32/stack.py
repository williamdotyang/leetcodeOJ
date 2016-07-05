class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
                
        if len(stack) == 0:
            return len(s)
        max_num = 0
        last = len(s)
        while len(stack) > 0:
            index = stack.pop()
            num = last - index - 1
            max_num = max(max_num, num)
            last = index
        max_num = max(max_num, last)
    
        return max_num
