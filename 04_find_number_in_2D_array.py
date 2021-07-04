class Solution(object):
    # 直角坐标系法
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        x, y = 0, row - 1

        while x < col and y >= 0:
            if target < matrix[y][x]:
                y -= 1
            elif target > matrix[y][x]:
                x += 1
            else:
                return True
        return False
