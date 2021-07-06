class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1, f2 = 0, 1
        f3 = 0
        for i in range(2, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3 % 1000000007  # I do not know why % 10000000007

