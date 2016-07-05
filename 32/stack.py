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
        count = 0
        for j in range(0, len(s)):
            i = len(s) - j - 1
            if len(stack) > 0 and stack[-1] == i:
                if count > max_num:
                    max_num = count
                stack.pop()
                count = 0
            else:
                count += 1
        if count > max_num:
            max_num = count
            
        return max_num
