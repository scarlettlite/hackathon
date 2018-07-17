import heapq

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        chardict = {}
        for x in s:
            if chardict.get(x) == None:
                chardict[x] = 1
            else:
                chardict[x] += 1
        heap = [(value,key) for key,value in chardict.items()]
        heap = heapq.nlargest(len(heap), heap)
        ans = ""
        for f,ch in heap:
            for i in range(f):
                ans += ch
        return ans

print(Solution().frequencySort("raaeaedere"))