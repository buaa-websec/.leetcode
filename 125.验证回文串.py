#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        a = ''.join(filter(str.isalnum, s)).lower()
        b = a[::-1]
        return (a==b)
# @lc code=end

