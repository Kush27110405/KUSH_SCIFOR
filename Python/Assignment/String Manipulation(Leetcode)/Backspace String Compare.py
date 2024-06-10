"""
Question:-
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        a = ""
        b = ""
        item = ''
        for i in range(0,len(s)):
            if s[i] == '#':
                if len(stack1) > 0:
                    item = stack1.pop()
                else:
                    continue
            else:
                stack1.append(s[i])
        while len(stack1) > 0:
            a += stack1.pop()
        for i in range(0,len(t)):
            if t[i] == '#':
                if len(stack2) > 0:
                    item = stack2.pop()
                else:
                    continue
            else:
                stack2.append(t[i])
        while len(stack2) > 0:
            b += stack2.pop()
        if a == b:
            return True
        else:
            return False
