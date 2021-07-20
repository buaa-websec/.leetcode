#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:  
        if x == 0: return 0
        if x == 1: return 1
        if x == 2: return 1
        for i in range(x):
            if i**2 > x:
                return i-1

# @lc code=end

