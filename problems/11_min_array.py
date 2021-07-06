class Solution(object):
    """
    leetcode related problems:
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
    """
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if len(numbers) == 1:
            return numbers[0]
        min_ = numbers[0]
        for n in numbers:
            if n < min_:
                min_ = n
        return min_