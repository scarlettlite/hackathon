from collections import deque

class DefaultInfDict(dict):
    def __missing__(self, key):
        self[key] = float('inf')
        return self[key]
class Solution:
    def prefixmatch(self, A, B):
        k = 0
        for a,b in zip(A,B):
            if a == b: 
                k += 1
            else:
                break
        return k

    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) != len(B) : return 0
        n = len(A)
        disdict = DefaultInfDict()
        queue = deque([(0, A)])
        disdict[A] = 0
        n = len(A)
        while queue:
            dis, src = queue.popleft()
            if src == B:
                return dis
            if dis > disdict[src]: 
                continue
            arr = list(src)
            x = self.prefixmatch(B, src)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        arr[i], arr[j] = arr[j], arr[i]
                        tgt = ''.join(arr)
                        arr[i], arr[j] = arr[j], arr[i]
                        y = self.prefixmatch(B, tgt)
                        if dis+1 < disdict[tgt] and y > x:
                            queue.append((dis+1, tgt))
                            disdict[tgt] = dis + 1
        return -1

print(Solution().kSimilarity("abcdefabcdef", "adecbffdecab"))

