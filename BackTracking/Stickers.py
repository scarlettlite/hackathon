from collections import Counter
class Solution:
    def __init__(self):
        pass

    def helper(self, target, i, stickers, count, mincurr):
        n = len(stickers)
        if all([value <= 0 for value in target.values()]):
            return count
        if count >= mincurr:
            return float('inf')
        for j in range(i, n):
            newtarget = target - stickers[j];
            if all([newtarget[key] == target[key]  for key in target.keys()]):
                continue
            mincurr = min(mincurr, self.helper(newtarget, j, stickers, count+1, mincurr))
        return mincurr

    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target = Counter(target)
        stickers = [Counter(s) & target for s in stickers]
        n = len(stickers)
        """
        please note the way to exclude items in an array
        when we change the list while going through it
        """
        for i,x in enumerate(stickers):
            if x != None:
                for j, y in enumerate(stickers):
                        if x & y == y:
                            stickers[j] = None
        stickers = list(filter(lambda x: x != None, stickers))
        result = self.helper(target, 0, stickers, 0, float('inf'))
        if result == float('inf'):
            result = -1
        return result

print(Solution().minStickers(["city","would","feel","effect","cell","paint"], "putcat"))



        