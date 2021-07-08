class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.m = m
        self.n = n
        self.k = k
        self.visited = set()
        # do not use for loop to each, just start from [0, 0]
        self.backtrack(0, 0)
        return self.count

    def backtrack(self, i, j):
        # cross the board and stop the search
        if i == -1 or j == -1 or i == self.m or j == self.n:
            return

        if (i, j) in self.visited:
            return

        if self.sums(i) + self.sums(j) > self.k:
            return

        self.count += 1

        self.visited.add((i, j))

        self.backtrack(i, j - 1)
        self.backtrack(i, j + 1)
        self.backtrack(i - 1, j)
        self.backtrack(i + 1, j)

        # self.visited.remove((i, j))

    def sums(self, x):
        s = 0
        while x != 0:
            s += x % 10
            x = x // 10
        return s
