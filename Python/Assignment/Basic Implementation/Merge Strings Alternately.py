"""
Question :-
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        m = len(word1)
        n = len(word2)
        ans = ""
        for i in range(0,min(m,n)):
            ans += word1[i]
            ans += word2[i]
        if i < m - 1:
            for i in range(i+1,m):
                ans += word1[i]
        if i < n - 1:
            for i in range(i+1,n):
                ans += word2[i]
        return ans

        
