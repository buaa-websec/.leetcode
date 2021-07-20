#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        
        if s[0] == '-':
            num = int(s[-1:0:-1])
            if num > 2**31:
                return 0
            return -num
        else: 
            num = int(s[::-1])
            if num > 2**31-1:
                return 0
            return num

# @lc code=end

