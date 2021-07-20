#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a = 1
        while n >= a:
            if n == a:
                return True
            a = a*3
        return False
# @lc code=end

