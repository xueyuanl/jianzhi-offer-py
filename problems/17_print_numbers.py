class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        big_number = 10 ** n - 1

        for i in range(1, big_number + 1):
            res.append(i)

        return res