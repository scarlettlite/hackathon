class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        l = dominoes
        n = len(l)
        force = [0]*n
        f = 0
        for i in range(n):
            if l[i] == 'R':
                f = n
            elif l[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f
        for i in range(n-1,-1,-1):
            if l[i] == 'L':
                f = n
            elif l[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f
        
        return ''.join(['.' if f == 0 else 'R' if f > 0 else 'L' for f in force])

print(Solution().pushDominoes("RRRR.....LLLL"))