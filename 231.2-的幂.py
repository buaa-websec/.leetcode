#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a = 1
        while n >= a:
            if n == a:
                return True
            a = a*2
        return False
            
# @lc code=end

