# from collections import defaultdict
# from math import factorial
# def npr(n, r):
#     numer = factorial(n)
#     denom = factorial(n-r)
#     return numer//denom

# class Solution:
#     def getdis(self, p1, p2):
#         return pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1],2)

#     def numberOfBoomerangs(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         dd = defaultdict(int)
#         n = len(points)
#         for i in range(n):
#             for j in range(n):
#                 x, y = points[i], points[j]
#                 dd[self.getdis(x,y), tuple(x)] += 1
#         count = 0
#         for x in dd.values():
#             if x > 1:
#                 count += npr(x, 2)
#         return count

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result=0
        for [i,j] in points:
            distance={}
            for [x,y] in points:
                dist_ij=(i-x)*(i-x)+(j-y)*(j-y)
                if dist_ij in distance:
                    result+=distance[dist_ij]
                    distance[dist_ij]+=1  
                else:
                    distance[dist_ij]=1
        return result*2

print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))           

        