def getText(s):
    text = ""
    for x in s.lower():
        if x.isalpha():
            text += x
    print(text)
    return text

def isPal_rec(s):
    if s == "" or len(s) == 0:
        return True
    return (s[0] == s[-1]) and isPal_rec(s[1:-1])

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return isPal_rec(getText(s))
