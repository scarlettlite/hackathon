class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return strs
        count = 0
        for i,x in enumerate(zip(*strs)):
            if all(strs[0][i] == a for a in x):
                count+=1
            else:
                break
        return strs[0][:count]

print(Solution().longestCommonPrefix(["ulower","flow","flight"]))