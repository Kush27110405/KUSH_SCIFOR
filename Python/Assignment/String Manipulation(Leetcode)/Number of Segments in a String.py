"""
Question:-
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        b = 0
        isnotspace = False
        for i in range(0,len(s)):
            if not(isnotspace) and s[i] == ' ':
                a += 1
                continue
            else:
                isnotspace = True
                break
        isnotspace = False
        for i in range(len(s) - 1, -1, -1):
            if not(isnotspace) and s[i] == ' ':
                b += 1
                continue
            else:
                isnotspace = True
                break
        ans = 0
        if b == len(s):
            return ans
        for i in range(a,len(s) - b):
            if s[i] != ' ':
                isnotspace = True
                continue
            elif isnotspace:
                isnotspace = False
                ans += 1
                continue
            else:
                continue
        return ans + 1
