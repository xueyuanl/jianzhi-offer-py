class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = []
        for c in s:
            if c == ' ':
                out.append('%20')
            else:
                out.append(c)
        return ''.join(out)

    # 或者原地扩充字符串，从后往前遍历
