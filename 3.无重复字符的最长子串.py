#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        first = 0
        l = 0
        l_max = 0
        
        substring = set()

        for i in range(len(s)):
            l += 1
            while s[i] in substring:
                substring.remove(s[first])
                first += 1
                l -= 1
            l_max = max(l, l_max)
            substring.add(s[i])
        return l_max    


# @lc code=end

