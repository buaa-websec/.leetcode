#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a = 1
        while n >= a:
            if n == a:
                return True
            a = a*4
        return False
# @lc code=end

