class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for n in nums:
            if n & 1 == 1:
                odd.append(n)
            else:
                even.append(n)
        odd.extend(even)
        return odd

    # two points, head and tail
    def exchange(self, nums):
        l, r = 0, len(nums) - 1

        while (l < r):
            while nums[l] & 1 == 1 and l < r:
                l += 1
            while nums[r] & 1 == 0 and l < r:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]

        return nums
