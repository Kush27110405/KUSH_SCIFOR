"""
Question:-
Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.
"""
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        x = int(math.sqrt(c))
        for b in range(x, -1, -1):
            a = math.sqrt(c - (b * b))
            if a == 0:
                return True
            elif int(a) == 0:
                continue
            else:
                if a % int(a) == 0:
                    return True
                else:
                    continue
        return False
        
