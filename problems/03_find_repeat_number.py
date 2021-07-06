class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0] * len(nums)
        for i in nums:
            if a[i] > 0:
                return i
            else:
                a[i] += 1
