def getrowcol(num):
    return divmod(num, 3)
from collections import defaultdict
class Solution:
    def helper(self, visited, last, step):
        vf = frozenset(visited)
        if (last, step, vf) in self.cache:
            return self.cache[(last, step, vf)]
        else:
            count = 0
            if step == 0:
                count += 1
            elif step > 0:
                for i in range(9):
                    if i not in visited:
                        ir, ic = getrowcol(i)
                        lr, lc = getrowcol(last)
                        flag = False
                        if ir == lr and abs(ic - lc) == 1:
                                flag = True
                        elif ic == lc and abs(ir - lr) == 1:
                                flag = True
                        elif abs(ir - lr) == 1 and abs(ic - lc) == 1:
                                flag = True
                        elif (i + last) // 2 in visited:
                            flag = True
                        elif i in self.ll[last]:
                            flag = True

                        if flag == True:
                            visited.add(i)
                            count += self.helper(visited, i, step-1)
                            visited.remove(i)
            self.cache[(last, step, vf)] = count
            return count
                

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.ll = {
            0:{5,7},
            1:{6,8},
            2:{3,7},
            3:{2,8},
            5:{0,6},
            6:{1,5},
            7:{0,2},
            8:{1,3}
        }
        self.cache = {}
        count = 0
        for step in range(m, n+1):
            x = self.helper(set({0}), 0, step-1)*4
            y = self.helper(set({1}), 1, step-1)*4
            z = self.helper(set({4}), 4, step-1)
            count+=(x+y+z)
        return count
#389497
print(Solution().numberOfPatterns(1,9))