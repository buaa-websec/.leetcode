#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return "" 
        pf = strs[0]
        for str in strs:
            if len(str) < len(pf):
                pf = pf[:len(str)]
                if len(pf) == 0: return ""
            for i in range(len(pf)):
                if pf[i] != str[i]:
                    pf = pf[:i]
                    break
        return pf


# @lc code=end

