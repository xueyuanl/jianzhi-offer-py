class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1  # mind the init value
        if n == 1:
            return 1
        f1, f2 = 1, 1
        f3 = 0
        for i in range(2, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3 % 1000000007