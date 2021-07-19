class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a, self.b = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.append(x)
        if not self.b or x <= self.b[-1]:
            self.b.append(x)

    def pop(self):
        """
        :rtype: None
        """
        aa = self.a.pop()
        if aa == self.b[-1]:
            self.b.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.b[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
