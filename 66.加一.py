#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = digits    
        for i in range(-1,-len(output)-1,-1):
            if output[i] == 9:
                output[i] = 0
            else:
                output[i] = output[i]+1
                return output
        output.insert(0, 1)
        return output
# @lc code=end

