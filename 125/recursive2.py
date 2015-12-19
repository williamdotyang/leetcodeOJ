def isPal_rec(s, i, j):
    if i >= j:
        return True
    if not s[i].isalpha():
        return isPal_rec(s, i+1, j)
    if not s[j].isalpha():
        return isPal_rec(s, i, j-1)
    return (s[i].lower() == s[j].lower()) and isPal_rec(s, i+1, j-1)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return isPal_rec(s, 0, len(s) - 1)
