#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while True:
            if len(s) == 1:
                return int(s)
            a = 0
            for i in range(len(s)):
                a += int(s[i])
            s = str(a) 
# @lc code=end

