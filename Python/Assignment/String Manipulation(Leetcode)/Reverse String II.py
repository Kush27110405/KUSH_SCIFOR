"""
Question:-
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        count = len(s)
        while (count - (2 * k)) >= 0:
            for i in range(len(s) - count + k - 1, len(s) - count - 1, -1):
                ans += s[i]
            for i in range(len(s) - count + k, len(s) - count + (2 * k)):
                ans += s[i]
            count -= (2 * k)
        if count < k:
            for i in range(len(s) - 1, len(s) - count - 1, -1):
                ans += s[i]
        else:
            for i in range(len(s) - count + k - 1, len(s) - count - 1, -1):
                ans += s[i]
            for i in range(len(s) - count + k, len(s)):
                ans += s[i]
        return ans
       
