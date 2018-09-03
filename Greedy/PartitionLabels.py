class Solution:
    def partitionLabels(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        ans, n = [-1], len(s)
        idxdict = {c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if i > ans[-1] and idxdict[c] > ans[-1]:
                ans.append(idxdict[c])
            elif idxdict[c] > ans[-1]:
                ans[-1] = idxdict[c]
        return [ans[i]-ans[i-1] for i in range(1, len(ans))]

print(Solution().partitionLabels("absbdeutiirqwmnlopmnlo"))