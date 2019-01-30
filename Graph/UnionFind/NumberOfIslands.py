class Solution:
    def numIslands2(self, m, n , positions):
        parent = { }
        directions = [ [1, 0], [-1, 0] ,[0, 1], [0, -1] ]
        islands_arr = [ ]
        islands = 0
        for r,c in positions:
            parent[(r, c)] = (r,c)
            neighbors = set( )
            for di, dj in directions:
                ir, ic = r + di, c + dj
                if 0 <= ir < m and 0 <= ic < n and (ir, ic) in parent:
                    neighbors.add(parent[(ir,ic)])
            if len(neighbors) > 0:
                new_parent = neighbors.pop()
                islands -= len(neighbors)
                for neighbor in neighbors:
                    parent[neighbor] = new_parent
            else:
                islands += 1
            islands_arr.append(islands)
        return islands_arr

print(Solution().numIslands2(3,3, [[0,0], [0,1], [1,2], [2,1], [1,1]]))