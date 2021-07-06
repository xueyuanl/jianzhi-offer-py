class CQueue(object):

    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.a.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.b:
            return self.b.pop()
        if not self.a:
            return -1
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()