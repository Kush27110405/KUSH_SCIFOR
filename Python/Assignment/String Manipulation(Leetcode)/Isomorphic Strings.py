"""
Question:
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Dict = {}
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            if any((Dict.get(j) == t[i] and j != s[i]) for j in Dict):
                return False
                break
            elif Dict.get(s[i]) == None:
                Dict[s[i]] = t[i]
            elif Dict.get(s[i]) == t[i]:
                continue
            else:
                return False
                break

        return True
        
