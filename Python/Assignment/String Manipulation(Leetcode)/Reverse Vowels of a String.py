"""
Question:-
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        u = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i].lower() == 'a' or s[i].lower() == 'e' or s[i].lower() == 'i' or s[i].lower() == 'o' or s[i].lower() == 'u':
                u += s[i]
        v = ""
        count = 0
        for i in range(0,len(s)):
            if not(s[i].lower() == 'a' or s[i].lower() == 'e' or s[i].lower() == 'i' or s[i].lower() == 'o' or s[i].lower() == 'u'):
                v += s[i]
            else:
                v += u[count]
                count += 1
        return v
