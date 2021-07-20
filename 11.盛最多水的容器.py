#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        v = 0
        while i < j:
            l = j - i
            if height[i] > height[j]:
                h = height[j]
                j = j - 1
            else:
                h = height[i]
                i = i + 1
            v = max(v, l * h)
        return v

# @lc code=end
